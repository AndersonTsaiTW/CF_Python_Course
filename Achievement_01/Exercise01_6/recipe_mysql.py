import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id   INT  PRIMARY KEY AUTO_INCREMENT,
               name   VARCHAR(50),
               ingredients  VARCHAR(255),
               cooking_time  INT,
               difficulty  VARCHAR(20)
)''')


def create_recipe(conn, cursor):
    name = str(input("recipe's name: "))
    cooking_time = int(input("cooking_time: "))
    ingredients = input("Enter the new ingredients (comma-separated): ")
    ingredients_list = [ingredient.strip().lower()
                        for ingredient in ingredients.split(",")]
    difficulty = calc_difficulty(cooking_time, ingredients_list)

    # insert data
    ingredients_string = ", ".join(ingredients_list)
    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    values = (name, ingredients_string, cooking_time, difficulty)
    cursor.execute(query, values)
    conn.commit()


def calc_difficulty(cooking_time, ingredients):
    difficulty = ""
    if (cooking_time < 10):
        if (len(ingredients) < 4):
            difficulty = "Easy"
        else:
            difficulty = "Medium"
    else:
        if (len(ingredients) < 4):
            difficulty = "Intermediate"
        else:
            difficulty = "Hard"
    return difficulty


def search_recipe(conn, cursor):
    # 1. Get the all_ingredients list
    query = "SELECT ingredients FROM Recipes"
    cursor.execute(query)
    results = cursor.fetchall()  # it will be a List of Tuples

    all_ingredients = set()

    for row in results:
        ingredients_list = row[0].split(", ")  # split by ", " to a list
        all_ingredients.update(ingredients_list)

    all_ingredients = list(all_ingredients)

    # 2. let the user choose from the list
    print("\nAvailable Ingredients:")
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(f"{index}. {ingredient}")

    choice = None
    while choice not in range(1, len(all_ingredients) + 1):
        try:
            choice = int(
                input("\nEnter the number of the ingredient to search for: "))
            if choice not in range(1, len(all_ingredients) + 1):
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            choice = None

    search_ingredient = all_ingredients[choice - 1]

    # 3. query from the database and display them
    query = """SELECT name, ingredients, cooking_time, difficulty 
           FROM Recipes 
           WHERE ingredients LIKE %s"""
    cursor.execute(query, (f"%{search_ingredient}%",))

    search_results = cursor.fetchall()
    if search_results:
        print("\nRecipes found:")
        for recipe in search_results:
            name, ingredients, cooking_time, difficulty = recipe
            print(
                f"\nName: {name}\n   Ingredients: {ingredients}\n   Cooking Time: {cooking_time} min\n   Difficulty: {difficulty}")
    else:
        print("\nNo recipes found with this ingredient.")


def update_recipe(conn, cursor):
    # 1. get and display all recipes
    cursor.execute(
        "SELECT id, name, ingredients, cooking_time, difficulty FROM Recipes")
    recipes = cursor.fetchall()

    if not recipes:
        print("\nNo recipes found in the database.")
        return

    # Display all available recipes
    print("\nAvailable Recipes:")
    for recipe in recipes:
        print(
            f"{recipe[0]}. {recipe[1]} (Cooking Time: {recipe[3]} min, Difficulty: {recipe[4]})")

    # 2. Ask the user to select a recipe to update
    recipe_id = -1
    while recipe_id not in [recipe[0] for recipe in recipes]:
        try:
            recipe_id = int(input("\nEnter the ID of the recipe to update: "))

            if recipe_id not in [recipe[0] for recipe in recipes]:  # Check if ID exists
                print("Invalid ID.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            recipe_id = -1  # Reset to invalid value to continue loop

    # 3️. Ask the user to select the column to update
    print("\nWhich column would you like to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")

    column_choice = input("Enter your choice (1-3): ")

    if column_choice == "1":
        column = "name"
        new_value = input("Enter the new recipe name: ")
    elif column_choice == "2":
        column = "cooking_time"
        try:
            new_value = int(input("Enter the new cooking time (in minutes): "))
        except ValueError:
            print("Invalid input. Cooking time must be a number.")
            return
    elif column_choice == "3":
        column = "ingredients"
        new_ingredients = input(
            "Enter the new ingredients (comma-separated): ")
        new_ingredients_list = [ingredient.strip().lower()
                                for ingredient in new_ingredients.split(",")]
        new_value = ", ".join(new_ingredients_list)
    else:
        print("Invalid choice.")
        return

    # 4️. Update the selected column in the database
    query = f"UPDATE Recipes SET {column} = %s WHERE id = %s"
    cursor.execute(query, (new_value, recipe_id))
    conn.commit()
    print(f"Recipe {recipe_id} updated successfully!")

    # 5️. If 'cooking_time' or 'ingredients' was updated, recalculate and update 'difficulty'
    if column in ["cooking_time", "ingredients"]:
        cursor.execute(
            # this , in  (recipe_id,) make it a tuple.
            # the second parameter in execute need a list or tuple
            "SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))

        updated_recipe = cursor.fetchone()
        new_cooking_time, new_ingredients = updated_recipe

        # Recalculate difficulty
        # Convert `new_ingredients` back into a list
        new_ingredients_list = new_ingredients.split(
            ", ")
        # Use the correct format for difficulty calculation
        new_difficulty = calc_difficulty(
            new_cooking_time, new_ingredients_list)
        cursor.execute(
            "UPDATE Recipes SET difficulty = %s WHERE id = %s", (new_difficulty, recipe_id))
        conn.commit()
        print(f"Difficulty updated to: {new_difficulty}")


def delete_recipe(conn, cursor):
    # 1️. Fetch all recipes
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    if not recipes:
        print("\nNo recipes found in the database.")
        return

    # Display all available recipes
    print("\nAvailable Recipes:")
    for recipe in recipes:
        print(f"{recipe[0]}. {recipe[1]}")  # Display ID and Name

    # 2️. Ask the user to select a recipe ID to delete
    valid_ids = [recipe[0] for recipe in recipes]  # Extract valid IDs
    recipe_id = -1  # Initialize with an invalid value

    while recipe_id not in valid_ids:
        try:
            recipe_id = int(input("\nEnter the ID of the recipe to delete: "))
            if recipe_id not in valid_ids:
                print("Invalid ID. Please select a valid recipe ID.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            recipe_id = -1  # Reset to keep the loop running

    # 3️. Confirm before deleting
    confirmation = input(
        f"!!! Are you sure you want to delete Recipe ID {recipe_id}? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        return

    # 4️. Execute DELETE query
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()  # Save changes
    print(f"Recipe ID {recipe_id} has been deleted successfully!")


def main_menu(conn, cursor):
    # initialize
    choice = ""

    # This is our loop running the main menu.
    # It continues to loop as long as the user
    # doesn't choose to quit.
    while choice != 'quit':
        print("What would you like to do? Pick a choice!")
        print("1. Creating a new recipe")
        print("2. Searching for a recipe by ingredient")
        print("3. Updating an existing recipe")
        print("4. Deleting a recipe")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice.lower() == 'quit':
            print("Exiting program...")
            conn.commit()
            conn.close()
            break
        else:
            print("Invalid choice. Please enter a number between 1-4 or 'quit'.")


# Main process
main_menu(conn, cursor)

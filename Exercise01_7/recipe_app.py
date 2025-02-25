# 1 connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base  # Notice!!
from sqlalchemy.types import Integer, String
from sqlalchemy import Column
from sqlalchemy import create_engine
engine = create_engine(
    "mysql+pymysql://cf-python:password@localhost/task_database")  # Notice!!

Base = declarative_base()  # Notice!!

Session = sessionmaker(bind=engine)
session = Session()


class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + " (" + self.difficulty + ")>"

    def __str__(self):
        return (
            f"{'='*40}\n"
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'='*40}\n"
        )

    def calculate_difficulty(self):
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")


Base.metadata.create_all(engine)


def create_recipe():
    # Get the recipe name
    name = input("Enter the recipe name (max 50 chars): ").strip()
    if len(name) == 0:
        print("Error: Name cannot be empty.")
        return
    if len(name) > 50:
        print("Error: Name is too long (max 50 chars).")
        return

    # Get cooking time
    cooking_time_input = input("Enter cooking time in minutes: ").strip()
    if not cooking_time_input.isnumeric():
        print("Error: Cooking time must be a number.")
        return
    cooking_time = int(cooking_time_input)

    # Get number of ingredients
    num_ingredients_input = input(
        "How many ingredients will you enter? ").strip()
    if not num_ingredients_input.isnumeric():
        print("Error: Please enter a valid number.")
        return
    num_ingredients = int(num_ingredients_input)
    if num_ingredients <= 0:
        print("Error: The number of ingredients must be greater than 0.")
        return

    # Get ingredients list
    ingredients = []
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ").strip()
        if len(ingredient) > 0:
            ingredients.append(ingredient)

    # Convert ingredient list to a comma-separated string
    ingredients_str = ", ".join(ingredients)

    # Create a new Recipe object
    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )

    # Calculate difficulty based on ingredients and cooking time
    recipe_entry.calculate_difficulty()

    # Add the recipe to the database and commit changes
    session.add(recipe_entry)
    session.commit()

    print("\nRecipe successfully added to the database.")
    print(recipe_entry)


def view_all_recipes():
    # Query all recipes
    recipes = session.query(Recipe).all()

    # If no recipes exist, inform the user and return to the main menu
    if not recipes:
        print("No recipes found in the database.")
        return None

    # Loop through and display each recipe
    for recipe in recipes:
        print(recipe)  # Calls the __str__() method of the Recipe class


def search_by_ingredients():
    # Check if the database has any entries
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return

    # Retrieve all ingredients from the database
    results = session.query(Recipe.ingredients).all()

    # Extract unique ingredients
    all_ingredients = set()
    for result in results:
        ingredient_list = result[0].split(", ")  # Convert string to list
        all_ingredients.update(ingredient_list)

    # Convert set to list for indexing
    all_ingredients = sorted(all_ingredients)

    # Display available ingredients
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")

    # Get user input for ingredient selection
    selected_number = input(
        "\nEnter the number of the ingredient to search for: ").strip()

    # Validate user input
    if not selected_number.isnumeric():
        print("Error: Please enter a valid number.")
        return

    selected_number = int(selected_number)
    if selected_number < 1 or selected_number > len(all_ingredients):
        print("Error: Selected number is out of range.")
        return

    # Get the ingredient name based on the user's selection
    search_ingredient = all_ingredients[selected_number - 1]

    # Query the database for recipes containing the selected ingredient
    matching_recipes = session.query(Recipe).filter(
        Recipe.ingredients.like(f"%{search_ingredient}%")).all()

    # Display results
    if matching_recipes:
        print("\nMatching Recipes:")
        for recipe in matching_recipes:
            print(recipe)  # Calls __str__() method
    else:
        print("\nNo recipes found with the selected ingredient.")


def edit_recipe():
    # Check if there are any recipes in the database
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("No recipes found in the database.")
        return

    # Retrieve all recipes (ID and name only)
    results = session.query(Recipe.id, Recipe.name).all()

    # Display available recipes
    print("\nAvailable recipes:")
    for recipe_id, name in results:
        print(f"{recipe_id}. {name}")

    # Get user selection
    recipe_id_input = input(
        "\nEnter the ID of the recipe you want to edit: ").strip()
    if not recipe_id_input.isnumeric():
        print("Error: Please enter a valid numeric ID.")
        return

    recipe_id = int(recipe_id_input)

    # Retrieve the selected recipe
    recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).one()
    if not recipe_to_edit:
        print("Error: No recipe found with the given ID.")
        return

    # Display editable attributes
    print("\nEditing Recipe:")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking Time: {recipe_to_edit.cooking_time} minutes")

    # Get user choice for editing
    attribute_choice = input(
        "\nEnter the number of the attribute you want to edit: ").strip()
    if attribute_choice not in {"1", "2", "3"}:
        print("Error: Invalid selection.")
        return

    # Update the selected attribute
    if attribute_choice == "1":
        new_name = input("Enter the new name (max 50 chars): ").strip()
        if len(new_name) == 0 or len(new_name) > 50:
            print("Error: Invalid name length.")
            return
        recipe_to_edit.name = new_name

    elif attribute_choice == "2":
        new_ingredients = []
        num_ingredients_input = input(
            "Enter the number of ingredients: ").strip()
        if not num_ingredients_input.isnumeric() or int(num_ingredients_input) <= 0:
            print("Error: Please enter a valid number.")
            return

        num_ingredients = int(num_ingredients_input)
        for i in range(num_ingredients):
            ingredient = input(f"Enter ingredient {i+1}: ").strip()
            if ingredient:
                new_ingredients.append(ingredient)

        recipe_to_edit.ingredients = ", ".join(new_ingredients)

    elif attribute_choice == "3":
        new_cooking_time_input = input(
            "Enter the new cooking time in minutes: ").strip()
        if not new_cooking_time_input.isnumeric():
            print("Error: Cooking time must be a number.")
            return

        recipe_to_edit.cooking_time = int(new_cooking_time_input)

    # Recalculate difficulty
    recipe_to_edit.calculate_difficulty()

    # Commit changes
    session.commit()
    print("\nRecipe updated successfully.")
    print(recipe_to_edit)


def delete_recipe():
    # Check if any recipes exist
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("No recipes found in the database.")
        return

    # Retrieve and display all recipes (ID and name only)
    results = session.query(Recipe.id, Recipe.name).all()
    print("\nAvailable recipes:")
    for recipe_id, name in results:
        print(f"{recipe_id}. {name}")

    # Get user input for the recipe ID to delete
    recipe_id_input = input(
        "\nEnter the ID of the recipe you want to delete: ").strip()
    if not recipe_id_input.isnumeric():
        print("Error: Please enter a valid numeric ID.")
        return

    recipe_id = int(recipe_id_input)

    # Retrieve the selected recipe
    recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe_to_delete:
        print("Error: No recipe found with the given ID.")
        return

    # Confirm deletion
    confirmation = input(
        f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        return

    # Delete the recipe and commit changes
    session.delete(recipe_to_delete)
    session.commit()
    print(f"Recipe '{recipe_to_delete.name}' has been deleted successfully.")


def main_menu():
    """Display the main menu and allow the user to interact with the recipe database."""

    valid_choices = {"1", "2", "3", "4", "5", "quit"}  # Set of valid choices
    choice = None  # Initialize choice variable

    while choice != "quit":
        print("\n===== Recipe Database Menu =====")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit the application.")

        # Get user input and validate
        choice = input("\nEnter your choice: ").strip().lower()

        if choice not in valid_choices:
            print("Error: Invalid input. Please enter a number from 1 to 5 or 'quit'.")
            continue  # Skip the rest of the loop and show the menu again

        # Execute the corresponding function
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("\nClosing database connection. Goodbye!")
            session.close()
            engine.dispose()


# Start the application
main_menu()
# Test the function
# delete_recipe()
# Test the function
# edit_recipe()
# search_by_ingredients()

import pickle


def display_recipe(rcp):
    print("")
    print(f"Recipe: {rcp['name']}")
    print(f"Cooking Time (min): {rcp['cooking_time']}")
    print("Ingredients:")
    for j in range(0, len(rcp['ingredients'])):
        print(rcp['ingredients'][j])
    print(f"Difficulty level: {rcp['difficulty']}")
    print("")


def search_ingredient(data):
    print("Available ingredients:")
    for index, ingredient in enumerate(data['all_ingredients']):
        print(f"{index}: {ingredient}")

    try:
        # let users choose index
        choice = int(input(
            "Enter the number of the ingredient you'd like to search for: "))
        ingredient_searched = data['all_ingredients'][choice]
    except (ValueError, IndexError):
        print("Invalid input! Please enter a valid number from the list.")
    else:
        # search the recipes including this ingredient
        print(f"Recipes containing '{ingredient_searched}':")
        found = False
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        if not found:
            print(
                f"No recipes found with the ingredient '{ingredient_searched}'.")


filename = input("Enter the filename of your recipe data: ")

try:
    # open file and get the data
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        print("File loaded successfully!")
except FileNotFoundError:
    # Alert users when file is not there
    print(
        f"The file '{filename}' was not found. Please check the filename and try again.")
else:
    # run search_ingredient(data) when we got the data
    search_ingredient(data)

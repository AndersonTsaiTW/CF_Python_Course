import pickle


def take_recipe():
    name = str(input("recipe's name: "))
    cooking_time = int(input("cooking_time: "))
    more = "Y"
    ingredients = []
    while more.upper() == "Y":
        ingredients.append(str(input("Enter your ingredients one-by-one: ")))
        more = input("Do you have more ingredients(Y/N)?: ")
    recipe = {'name': name, 'cooking_time': cooking_time,
              'ingredients': ingredients}
    calc_difficulty(recipe)
    return recipe


def calc_difficulty(rcp):
    if (rcp['cooking_time'] < 10):
        if (len(rcp['ingredients']) < 4):
            rcp['difficulty'] = "Easy"
        else:
            rcp['difficulty'] = "Medium"
    else:
        if (len(rcp['ingredients']) < 4):
            rcp['difficulty'] = "Intermediate"
        else:
            rcp['difficulty'] = "Hard"


filename = input("Enter the filename of recipes: ")
try:
    my_file = open(filename, 'rb')
    data = pickle.load(my_file)
except FileNotFoundError:
    print("File not found. Creating a new data structure.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
except Exception as e:
    print(f"An error occurred: {e}. Creating a new data structure.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
else:
    my_file.close()
finally:
    recipes_list = data.get('recipes_list', [])
    all_ingredients = data.get('all_ingredients', [])
    print("Data extracted:")
    print(f"Recipes: {recipes_list}")
    print(f"All Ingredients: {all_ingredients}")


# run take_recipe() several times to collect recipes from users
# Also, add new ingredients to the list
n = int(input("How many recipes you would like to enter: "))
for i in range(0, n):
    recipe = take_recipe()
    for ele in recipe['ingredients']:
        if ele not in all_ingredients:
            all_ingredients.append(ele)
    recipes_list.append(recipe)

# put the updated data in one dictionary
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

# update the data to the file
with open(filename, 'wb') as my_file:
    pickle.dump(data, my_file)


with open(filename, 'rb') as my_file:
    data = pickle.load(my_file)
    recipes_list = data.get('recipes_list', [])
    all_ingredients = data.get('all_ingredients', [])
    print("Updated Data extracted:")
    print(f"Recipes: {recipes_list}")
    print(f"All Ingredients: {all_ingredients}")

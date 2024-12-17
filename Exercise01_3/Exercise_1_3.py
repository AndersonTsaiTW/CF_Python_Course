recipes_list = []
ingredients_list = []


def take_recipe():
    name = str(input("recipe's name: "))
    cooking_time = int(input("cooking_time: "))
    more = "Y"
    ingredients = []
    while (more == "Y"):
        ingredients.append(str(input("Enter your ingredients one-by-one: ")))
        more = input("Do you have more ingredints(Y/N)?: ")
    recipe = {'name': name, 'cooking_time': cooking_time,
              'ingredients': ingredients}
    return recipe


n = int(input("How many recipes you would like to enter: "))
for i in range(0, n):
    recipe = take_recipe()
    for ele in recipe['ingredients']:
        if ele not in ingredients_list:
            ingredients_list.append(ele)
    recipes_list.append(recipe)

for rcp in recipes_list:
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

for i in range(0, n):
    print("")
    print(f"Recipe: {recipes_list[i]['name']}")
    print(f"Cooking Time (min): {recipes_list[i]['cooking_time']}")
    print("Ingredients:")
    for j in range(0, len(recipes_list[i]['ingredients'])):
        print(recipes_list[i]['ingredients'][j])
    print(f"Difficulty level: {recipes_list[i]['difficulty']}")
    print("")

print("Ingredients Available Across All Recipes")
print("-" * 40)
for i in range(0, len(ingredients_list)):
    print(ingredients_list[i])

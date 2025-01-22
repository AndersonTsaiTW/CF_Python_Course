class Recipe(object):
    all_ingredients = []

    def __init__(self, name, cooking_time=None, ingredients=None):
        self.name = name
        self.cooking_time = cooking_time if cooking_time is not None else 0
        self.ingredients = ingredients if ingredients is not None else []
        self.difficulty = self.calculate_difficulty()

    # Getter and Setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return f"Recipe name updated to: {self.name}"

    # Getter and Setter for cooking_time
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        if cooking_time < 0:
            return "Cooking time cannot be negative."
        else:
            self.cooking_time = cooking_time
            # Recalculate difficulty after updating cooking time
            self.difficulty = self.calculate_difficulty()
            return f"Cooking time updated to: {self.cooking_time} minutes"

    def add_ingredients(self, *new_ingredients):
        for ingredient in new_ingredients:
            if ingredient not in self.ingredients:  # Avoid duplicates
                self.ingredients.append(ingredient)
        self.update_all_ingredients()
        # update the difficulty
        self.difficulty = self.calculate_difficulty()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10:
            if len(self.ingredients) < 4:
                return "Easy"
            else:
                return "Medium"
        else:
            if len(self.ingredients) < 4:
                return "Intermediate"
            else:
                return "Hard"

    def get_difficulty(self):
        if self.difficulty is None:
            self.difficulty = self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        return (f"Recipe: {self.name}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Difficulty: {self.difficulty}\n")

    def recipe_search(data, search_term):
        found = False
        print(f"Recipes include \"{search_term}\" below:\n")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                found = True
        if not found:
            print(f"No recipes contain the ingredient '{search_term}'.")


tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
print(tea)

coffee = Recipe("Coffee", 5, ["Coffee Powder", "Sugar", "Water"])
cake = Recipe("Cake", 50, ["Sugar", "Butter", "Eggs",
              "Vanilla Essence", "Flour", "Baking Powder", "Milk"])
bananaSmoothie = Recipe("Banana Smoothie", 5, [
                        "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"])
recipes_list = [tea, coffee, cake, bananaSmoothie]

Recipe.recipe_search(recipes_list, "Water")
Recipe.recipe_search(recipes_list, "Sugar")
Recipe.recipe_search(recipes_list, "Bananas")

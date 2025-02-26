# Recipe Management System

This project demonstrates a simple **Recipe Management System** implemented using Python and the principles of **Object-Oriented Programming (OOP)**. It allows creating, managing, and searching recipes based on their ingredients, cooking time, and difficulty level.

## Features

1. **Class and Objects**:
   - The `Recipe` class represents a recipe with attributes like:
     - `name`: The name of the recipe.
     - `cooking_time`: The time required to cook.
     - `ingredients`: A list of ingredients.
     - `difficulty`: Automatically calculated based on `cooking_time` and `ingredients`.

2. **Ingredient Management**:
   - Add ingredients to a recipe while avoiding duplicates.
   - Track all unique ingredients across all recipes with a class-level variable `all_ingredients`.

3. **Dynamic Difficulty Calculation**:
   - Automatically calculates difficulty based on:
     - Cooking time: `<10 minutes` or `>=10 minutes`.
     - Number of ingredients: `<4 ingredients` or `>=4 ingredients`.
   - Difficulty levels:
     - `Easy`, `Medium`, `Intermediate`, `Hard`.

4. **Search Functionality**:
   - Search for recipes that include a specific ingredient using `Recipe.recipe_search(data, search_term)`.
   - Displays all matching recipes or a message if no match is found.

## Code Overview

### Class Methods
- `__init__(name, cooking_time, ingredients)`: Initializes a new recipe object.
- `add_ingredients(*new_ingredients)`: Adds ingredients to a recipe.
- `calculate_difficulty()`: Calculates the difficulty level dynamically.
- `update_all_ingredients()`: Updates the class-level list of all ingredients.
- `search_ingredient(ingredient)`: Checks if a specific ingredient is in the recipe.
- `recipe_search(data, search_term)`: Searches for recipes containing a specific ingredient.
- `__str__()`: Returns a string representation of the recipe.

### Example Usage
```python
# Create recipes
tea = Recipe("Tea", 5, ["Tea Leaves", "Sugar", "Water"])
coffee = Recipe("Coffee", 5, ["Coffee Powder", "Sugar", "Water"])
cake = Recipe("Cake", 50, ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"])
bananaSmoothie = Recipe("Banana Smoothie", 5, ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"])

# Store recipes in a list
recipes_list = [tea, coffee, cake, bananaSmoothie]

# Search for recipes containing specific ingredients
Recipe.recipe_search(recipes_list, "Water")
Recipe.recipe_search(recipes_list, "Sugar")
Recipe.recipe_search(recipes_list, "Bananas")

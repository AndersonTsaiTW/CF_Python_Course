# Recipe Management System

This part is a **Python-based Recipe Management System** that allows users to **create, search, update, and delete recipes** using a MySQL database. It dynamically calculates **recipe difficulty** based on **cooking time and the number of ingredients**.

---

## Features
1. **Recipe Management**:
   - Add new recipes with a name, cooking time, and ingredients.
   - Update or delete existing recipes.

2. **Search Functionality**:
   - Search for recipes based on a specific ingredient.

3. **Automatic Difficulty Calculation**:
   - **Easy**: Cooking time < 10 min, ingredients < 4.
   - **Medium**: Cooking time < 10 min, ingredients ≥ 4.
   - **Intermediate**: Cooking time ≥ 10 min, ingredients < 4.
   - **Hard**: Cooking time ≥ 10 min, ingredients ≥ 4.

4. **Database Integration**:
   - Recipes are stored in a **MySQL database** for persistence.

---
## Run the code
python recipe_management.py

---

## Menu Options
Once you run the program, the following menu will appear:

   What would you like to do? Pick a choice!
   1. Creating a new recipe
   2. Searching for a recipe by ingredient
   3. Updating an existing recipe
   4. Deleting a recipe
   Type 'quit' to exit the program.

---

Feel free to try this program and give feedback
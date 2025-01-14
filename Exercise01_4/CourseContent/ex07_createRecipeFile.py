import pickle

# data example
example_data = {
    'recipes_list': [
        {
            'name': 'Pancakes',
            'cooking_time': 15,
            'ingredients': ['Flour', 'Milk', 'Eggs', 'Sugar'],
            'difficulty': 'Hard'
        },
        {
            'name': 'Salad',
            'cooking_time': 5,
            'ingredients': ['Lettuce', 'Tomato', 'Cucumber'],
            'difficulty': 'Easy'
        },
        {
            'name': 'Sandwich',
            'cooking_time': 10,
            'ingredients': ['Bread', 'Cheese', 'Ham'],
            'difficulty': 'Intermediate'
        },
        {
            'name': 'Pizza',
            'cooking_time': 20,
            'ingredients': ['Flour', 'Yeast', 'Tomato Sauce', 'Cheese', 'Pepperoni'],
            'difficulty': 'Hard'
        }
    ],
    'all_ingredients': [
        'Flour', 'Milk', 'Eggs', 'Sugar', 'Lettuce', 'Tomato',
        'Cucumber', 'Bread', 'Cheese', 'Ham', 'Yeast', 'Tomato Sauce', 'Pepperoni'
    ]
}

# store data to file
filename = 'example_data.pkl'
with open(filename, 'wb') as file:
    pickle.dump(example_data, file)

print(f"Example file '{filename}' has been created successfully!")

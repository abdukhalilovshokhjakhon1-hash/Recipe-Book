# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
recipes = [
    {
        'name': 'pancakes',
        'ingredients': [
            "All-purpose flour",
            "Baking powder",
            "White sugar",
            "Table salt",
            "Whole milk",
            "Large egg",
            "Melted butter",
            "Vanilla extract"
        ],
        'steps': [
            "Whisk dry ingredients.",
            "Blend wet ingredients.",
            "Combine mixtures gently.",
            "Preheat greased skillet.",
            "Pour the batter.",
            "Flip until golden.",
            "Serve warm."
        ]
    }
]

def show_recipes(recipes):
    for i, recipe in enumerate(recipes):
        print(f'{i+1}. {recipe["name"]}')

show_recipes(recipes)

# A way for the user to view the said recipe

def show_recipe_details(recipes, recipe_index):
    details=f'{recipes[recipe_index]['name']} \n ==== Ingredients ====\n'
    for ingredient in recipes[recipe_index]['ingredients']:
        details += f' - {ingredient} \n'
    details+= '==== Steps ====\n'
    for step, info in enumerate(recipes[recipe_index]['steps']):
        details += f'{step+1}. {info} \n'

    return details


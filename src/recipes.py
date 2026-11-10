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
    },
]

def show_recipes(recipes=recipes):
    output=''
    for index, details in enumerate(recipes):
        output+= f'{index + 1}. {details["name"]}\n'
    return output if output else 'You have no recipes'




def add_recipe(details):
    recipes.append(details)
    print(f'Recipe {details["name"]} added!')



def show_recipe_details(recipe_index):
    details=f'{recipes[recipe_index]['name']} \n ==== Ingredients ====\n'
    for ingredient in recipes[recipe_index]['ingredients']:
        details += f' - {ingredient} \n'
    details+= '==== Steps ====\n'
    for step, info in enumerate(recipes[recipe_index]['steps']):
        details += f'{step+1}. {info} \n'

    return details





def edit_recipe(recipe_index, details):
    recipes[recipe_index].update(details)
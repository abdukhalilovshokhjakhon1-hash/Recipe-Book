from recipes import *

def make_recipes(number=0):
    return \
        [
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
def make_recipe():
    return {
        'name': 'Cake',
        'ingredients': ['dough', 'egg'],
        'steps': [
            'Whisk dry ingredients.',
            'Blend wet ingredients.',
            'Bake'
        ]
    }
def test_show_recipes_returns_recipe_names():
    '''tests show_recipes returns the list of recipe names'''
    recipes = make_recipes()
    assert show_recipes(recipes)=='1. pancakes\n'

def test_show_recipes_tells_if_recipes_is_empty():
    '''tests show_recipes returns lets the user know if there are no recipes'''
    recipes=[]
    assert show_recipes(recipes)=='You have no recipes'

def test_show_recipes():
    test_show_recipes_returns_recipe_names()
    test_show_recipes_tells_if_recipes_is_empty()



def test_add_recipe():
    recipe = make_recipe()
    add_recipe(recipe)
    assert recipes==[
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
            {
                'name': 'Cake',
                'ingredients': ['dough', 'egg'],
                'steps': [
                    'Whisk dry ingredients.',
                    'Blend wet ingredients.',
                    'Bake'
                ]
            },
        ]

def test_edit_recipe():
    make_recipe()
    edit_recipe(0, {'name': 'Cake'})
    assert recipes[0]['name'] == 'Cake'


from recipes import *
import os

def show_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(show_recipes())
        choice = input(f'''
        1. View Recipe \n
        2. Add recipe \n
        3. Edit recipe \n
        4. Exit \n
        Please select an option from the menu:''')
        choice=choice.strip()
        if not choice.isdigit():
            continue
        choice=int(choice)
        if choice not in range(1,5):
            continue
        return choice

def pick_action(action):
    if action == 1:
        print(show_recipes())
        recipe=pick_recipe()
        print(show_recipe_details(recipe))
        input('Press enter to continue')
    elif action == 2:
        recipe=input_add_recipe()
        add_recipe(recipe)
        input('Press enter to continue')
    elif action == 3:
        recipe=pick_recipe()
        while True:
            change=input(
                         "1. Name \n"
                         "2. Ingredients\n"
                         "3. Steps\n"
                         "Pick what you want to change: \n"
            ).strip()
            if not change.isdigit():
                print("Please select an option from the menu.")
                continue
            if change == '1':
                change_detail='name'
            elif change == '2':
                change_detail='ingredients'
            elif change == '3':
                change_detail='steps'
            else:
                print("Please select an option from the menu.")
                continue
            change_detail=input_add_detail(change_detail)
            edit_recipe(recipe, change_detail)
            input('Press enter to continue')
            break
    else:
        return False





def menu():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("============Welcome to your Recipe Book============")
        choice=show_menu()
        if not pick_action(choice):
            break



    print('============Have A Great Day==========')

def input_add_recipe():
    name=input_add_detail('name')
    ingredients=input_add_detail('ingredients')
    steps=input_add_detail('steps')
    added_recipe={'name':name, 'ingredients':ingredients, 'steps':steps}
    return added_recipe

def input_add_detail(detail):
    if detail=='name':
        return input('Enter recipe Name:')
    added_details=[]
    while True:
        added_detail = input(f"Enter {detail}, or press enter to finish:")
        if not added_detail:
            break
        added_details.append(added_detail.strip())
    return added_details
def pick_recipe():
    while True:
        recipe=input('Enter recipe index:')
        if recipe.isdigit():
            recipe=int(recipe)-1
            if recipe<=len(recipes)-1:
                return recipe
            else:
                print('There is no such recipe, try again!')
                input('Press enter to continue')
                continue
        print("Sorry, this recipe does not exist, try again")
        input("Press enter to continue")
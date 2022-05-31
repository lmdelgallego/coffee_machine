from menu import MENU

resources = {
    "water": 50,
    "milk": 200,
    "coffee": 100,
}

profit = 0


# TODO: 2. Check resources sufficient to make drink order

def something_else():
    choice = input("Do you want something else? ( Y / N ) : ")
    return choice.lower() == 'y'


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_sufficient_resource(drink):
    menu_drink = MENU.get(drink.lower())
    if menu_drink is not None:
        drink_ingredients = menu_drink['ingredients']
        if int(drink_ingredients['water']) > int(resources['water']):
            print("Sorry there is not enough water.")
            return False
    else:
        return "heeeeeee"


def coffee_machine():
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice.lower() == "report":
        print_report()

    print(check_sufficient_resource(choice))

    if choice.lower() != 'off':
        coffee_machine()
    elif choice.lower() == 'off':
        print("Bye")


coffee_machine()

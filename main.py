from menu import MENU

resources = {
    "water": 50,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def something_else():
    choice = input("Do you want something else? ( Y / N ) : ")
    return choice.lower() == 'y'


def drink_select(drink):
    """Return drink for the dictionary"""
    return MENU.get(drink.lower())


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def process_coins():
    total = 0
    print("Please insert coins.")
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def check_sufficient_resource(drink_ingredients):
    """Check the resource for actual drink and return True o False"""
    is_enough = True
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


def coffee_machine():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    drink_selected = drink_select(choice)
    if choice.lower() == "report":
        print_report()

    if drink_selected is not None:
        check_sufficient_resource(drink_selected["ingredients"])

    if choice.lower() != 'off':
        coffee_machine()
    elif choice.lower() == 'off':
        print("Bye")


coffee_machine()

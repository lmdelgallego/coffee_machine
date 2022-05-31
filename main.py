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
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
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


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def coffee_machine():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    drink_selected = drink_select(choice)
    if choice.lower() == "report":
        print_report()

    if drink_selected is not None:
        if check_sufficient_resource(drink_selected["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink_selected['cost'])


    if choice.lower() != 'off':
        coffee_machine()
    elif choice.lower() == 'off':
        print("Bye")


coffee_machine()

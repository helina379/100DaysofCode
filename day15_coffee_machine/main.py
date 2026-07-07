MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print report of all coffee machine resources.

coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
print("Please insert coins.")
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickles = int(input("How many nickles?: "))
pennies = int(input("How many pennies?: "))

amount_given = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

# print(MENU[coffee_choice]["ingredients"]["water"])
# print("☕")

# if amount_given > MENU[coffee_choice]["cost"]:
#     change = amount_given - MENU[coffee_choice]["cost"]
#     print(f"Here is your change: ${change}")

# for coffee in MENU[coffee_choice]:
#     print(coffee)

def coffee_machine(coffee_type, amount):
    for coffee in MENU[coffee_type]:
        # if coffee == coffee_type:
            if amount >= MENU[coffee_type]["cost"]:
                change = amount - MENU[coffee_type]["cost"]
                if MENU[coffee_type]["ingredients"]["water"] <= resources["water"]:
                    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
                    if MENU[coffee_type]["ingredients"]["milk"] <= resources["milk"]:
                        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
                        if MENU[coffee_type]["ingredients"]["coffee"] <= resources["coffee"]:
                            resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
                            print(f"Here is your {coffee_type}: ☕")
                            if change > 0:
                                print(f"Here is your change: {change}")
                        else:
                            print("Sorry, there is not enough coffee")
                    else:
                        print("Sorry, there is not enough milk.")
                else:
                    print("Sorry, there is not enough water!")
            else:
                print("Sorry, you don't have enough money!")



coffee_machine(coffee_choice, amount_given)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()

money = MoneyMachine()

cofee_machine = CoffeeMaker()


want_coffee = "y"
while want_coffee == "y":
    coffee_choice = input(f"What coffee would u like? {menu.get_items()} ").lower()

    if coffee_choice == "report":
        cofee_machine.report()
        money.report()
        want_coffee = input("Do you want coffee? (y/n) ").lower()
    else:
        drink = menu.find_drink(coffee_choice) #checks if the user entered a coffee which is not on the menu

        cost = 0
        if drink:
            cost = drink.cost
            print(f"That'll be: ${cost}")

        if not drink:
            print("That's an invalid coffee choice.")
            want_coffee = input("Do you want more coffee? (y/n) ").lower()
            continue


        # money.make_payment(cost)
        # money.report() #report of the money in the coffee machine (profit)

        # print(cofee_machine.is_resource_sufficient(drink))
        if cofee_machine.is_resource_sufficient(drink) and money.make_payment(cost):
            cofee_machine.make_coffee(drink)
        else:
            print("Money refunded")
            # money.profit -= cost

        want_coffee = input("Do you want more coffee? (y/n) ").lower()

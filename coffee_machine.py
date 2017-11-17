"""
Coffee Machine Main Module

This module ties together the coffee maker, menu, and money machine to simulate a coffee machine.
It continuously prompts the user for a selection, processes orders, handles resource reports,
and deals with the payment system until the machine is turned off.
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    """
    The main function that runs the coffee machine simulation.

    It creates instances of the CoffeeMaker, Menu, and MoneyMachine, then enters a loop
    where it prompts the user for a drink selection, processes commands such as "report" or "off",
    and handles the purchase and preparation of the selected drink.
    """
    machine = CoffeeMaker()  # Instance handling coffee preparation and resource management.
    machine_menu = Menu()  # Instance managing the available drinks.
    machine_money = MoneyMachine()  # Instance handling money transactions.
    machine_on = True  # Control flag to keep the machine running.

    # Main loop for processing user input
    while machine_on:
        # Display available items and prompt the user for input
        user_drink = input("Please make a selection " + machine_menu.get_items() + ": ").lower()

        # Command to turn off the machine
        if user_drink == "off":
            print("Turning off the coffee machine. Goodbye!")
            machine_on = False
        # Command to display current resources and money
        elif user_drink == "report":
            machine.report()  # Prints the CoffeeMaker resource report.
            machine_money.report()  # Prints the MoneyMachine profit report.
        else:
            # Attempt to find the drink from the menu
            drink = machine_menu.find_drink(user_drink)
            if drink is not None:
                # Check if there are enough resources to prepare the selected drink.
                if machine.is_resource_sufficient(drink):
                    # Process the payment; proceed only if the transaction is successful.
                    if machine_money.make_payment(drink.cost):
                        machine.make_coffee(drink)  # Prepare and serve the drink.


# Run the coffee machine simulation.
main()

class CoffeeMaker:
    """Models the machine that makes the coffee by managing ingredient resources."""

    def __init__(self):
        # Initial resources in the coffee machine.
        self.resources = {
            "water": 300,  # in milliliters
            "milk": 200,  # in milliliters
            "coffee": 100,  # in grams
        }

    def report(self):
        """
        Prints a report of all available resources.

        Displays current water, milk, and coffee amounts.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Checks if there are sufficient resources to make the selected drink.

        Args:
            drink: A MenuItem object containing the drink's ingredients and cost.

        Returns:
            bool: True if the machine has enough resources; otherwise, False.
        """
        can_make = True
        # Loop over each ingredient needed for the drink.
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """
        Deducts the required ingredients from the resources and serves the coffee.

        Args:
            order: A MenuItem object representing the drink to be made.
        """
        # Deduct each ingredient used for the drink.
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

class MenuItem:
    """Models each Menu Item with a name, cost, and required ingredients."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        # Dictionary holding the required amounts of each ingredient.
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu containing available drinks."""

    def __init__(self):
        # Create a list of MenuItem objects representing the drink options.
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """
        Returns a string of available drink names separated by a slash.

        Example output: "latte/espresso/cappuccino/"
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """
        Searches for a drink by name in the menu.

        Args:
            order_name (str): The name of the drink to search for.

        Returns:
            MenuItem: The corresponding MenuItem if found; otherwise, None.
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

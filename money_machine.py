class MoneyMachine:
    """
    Models the money machine handling coin transactions and keeping track of profit.

    Attributes:
        CURRENCY (str): The currency symbol.
        COIN_VALUES (dict): A dictionary of coin types and their corresponding values.
    """

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0  # Total profit accumulated.
        self.money_received = 0  # Total money inserted by the user in a transaction.

    def report(self):
        """
        Prints the current profit earned by the machine.
        """
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """
        Prompts the user to insert coins and calculates the total amount received.

        Returns:
            float: The total amount of money inserted.
        """
        print("Please insert coins.")
        # Iterate through each coin type, ask the user for the count, and update money_received.
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """
        Processes a payment transaction for a drink.

        Args:
            cost (float): The cost of the drink.

        Returns:
            bool: True if the payment is sufficient and accepted; otherwise, False.
        """
        self.process_coins()
        # Check if the inserted money is enough to cover the cost.
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost  # Update profit with the cost of the drink.
            self.money_received = 0  # Reset money received for the next transaction.
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

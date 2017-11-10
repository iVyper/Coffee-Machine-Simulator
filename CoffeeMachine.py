"""
CoffeeMachine module

This module simulates a coffee machine that allows users to purchase various coffee drinks.
It manages ingredient storage, coin processing, and transaction updates while providing
a command-line interface for interaction.
"""

# Coffee machine configuration including available flavors and ingredient storage.
coffee_machine = {
    "flavors": {
        "espresso": {
            "water": 1.69,
            "coffee": 0.61,
            "price": 1.50,
        },
        "latte": {
            "water": 6.76,
            "coffee": 0.81,
            "milk": 5.07,
            "price": 2.50,
        },
        "cappuccino": {
            "water": 8.45,
            "coffee": 0.81,
            "milk": 3.38,
            "price": 3.00,
        },
    },
    "storage": {
        "water": 16.0,
        "milk": 10.0,
        "coffee": 10.0,
        "money": {
            "total_money": 0.00,
            "penny": {"value": 0.01, "stored": 0},
            "nickel": {"value": 0.05, "stored": 0},
            "dime": {"value": 0.10, "stored": 0},
            "quarter": {"value": 0.25, "stored": 0},
        },
    },
}


def generate_report():
    """
    Generates a report of the current ingredient and money storage levels.

    This function prints the remaining amounts of water, milk, coffee,
    and the total money stored in the machine.
    """
    storage = coffee_machine["storage"]
    print(f"Water: {storage['water']:.1f}oz")
    print(f"Milk: {storage['milk']:.1f}oz")
    print(f"Coffee: {storage['coffee']:.1f}oz")
    print(f"Money: ${storage['money']['total_money']:.2f}")


def check_resources(selection):
    """
    Check that there are enough resources to make the selected drink.

    Args:
        selection (str): The type of coffee drink selected (e.g., 'espresso', 'latte').

    Returns:
        bool: True if resources are sufficient; otherwise, prints an error and returns False.
    """
    ingredients = coffee_machine["flavors"][selection]
    # Loop through each required ingredient except the price.
    for ingredient, amount in ingredients.items():
        if ingredient == "price":
            continue
        available = coffee_machine["storage"].get(ingredient, 0)
        if amount > available:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def deduct_resources(selection):
    """
    Deducts the required ingredients from storage for the selected drink.

    Args:
        selection (str): The type of coffee drink selected.
    """
    ingredients = coffee_machine["flavors"][selection]
    # Subtract each ingredient (ignoring the price) from the storage.
    for ingredient, amount in ingredients.items():
        if ingredient != "price":
            coffee_machine["storage"][ingredient] -= amount


def process_coins():
    """
    Processes coin inputs from the user and calculates the total amount inserted.

    Prompts the user for the number of quarters, dimes, nickels, and pennies,
    ensuring that valid integers are provided.

    Returns:
        dict: A dictionary containing the counts for each coin type and the total value.
    """
    while True:
        try:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            break
        except ValueError:
            print("Please enter valid integers for the coin counts.")
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return {
        "quarters": quarters,
        "dimes": dimes,
        "nickels": nickels,
        "pennies": pennies,
        "total": total,
    }


def calculate_change(inserted, cost):
    """
    Calculates and returns the change due.

    Args:
        inserted (float): The total amount of money inserted.
        cost (float): The cost of the selected drink.

    Returns:
        float: The change due, rounded to 2 decimal places.
    """
    return round(inserted - cost, 2)


def update_money_storage(coin_data, cost):
    """
    Updates the money storage by adding the cost of the drink and updating the coin counts.

    Args:
        coin_data (dict): The coin counts and total inserted.
        cost (float): The cost of the drink.
    """
    money = coffee_machine["storage"]["money"]
    # Add only the cost to the total money storage.
    money["total_money"] += cost
    # Update the stored count for each coin type.
    money["quarter"]["stored"] += coin_data["quarters"]
    money["dime"]["stored"] += coin_data["dimes"]
    money["nickel"]["stored"] += coin_data["nickels"]
    money["penny"]["stored"] += coin_data["pennies"]


def make_coffee(selection):
    """
    Makes the coffee by checking resources and deducting them if sufficient.

    Args:
        selection (str): The type of coffee drink selected.

    Returns:
        bool: True if the coffee was successfully made; otherwise, False.
    """
    if not check_resources(selection):
        return False
    deduct_resources(selection)
    print(f"Here's your {selection}. Enjoy!")
    return True


def purchase(selection):
    """
    Handles the purchase process for the selected coffee drink.

    This function:
    - Displays the cost of the drink.
    - Processes coin input from the user.
    - Checks if the inserted money is sufficient.
    - Returns change if necessary.
    - Attempts to make the coffee and updates the money storage if successful.

    Args:
        selection (str): The type of coffee drink selected.
    """
    cost = coffee_machine["flavors"][selection]["price"]
    print(f"The price of {selection} is ${cost:.2f}. Please insert coins.")
    coin_data = process_coins()
    # Check if the inserted coins cover the cost of the drink.
    if coin_data["total"] < cost:
        print(f"Sorry, that's not enough money. Money refunded: ${coin_data['total']:.2f}")
        return

    # Calculate and print any change due.
    change = calculate_change(coin_data["total"], cost)
    if change > 0:
        print(f"Here is your ${change:.2f} in change.")

    # Make the coffee and update money storage if successful.
    if make_coffee(selection):
        update_money_storage(coin_data, cost)


def main():
    """
    The main loop for the coffee machine simulation.

    It continuously prompts the user for a command:
    - 'espresso', 'latte', or 'cappuccino' to purchase a drink.
    - 'report' to display current storage levels.
    - 'off' to shut down the machine.
    """
    while True:
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if selection == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif selection == "report":
            generate_report()
        elif selection in coffee_machine["flavors"]:
            purchase(selection)
        else:
            print("Invalid input. Please try again.")


# Start the coffee machine simulation.
main()

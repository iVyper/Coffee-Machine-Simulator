# Coffee Machine Simulator
This project simulates a real-world coffee machine through a command-line interface. The application is organized into several modules that handle different aspects of the coffee-making process, including drink selection (Menu), ingredient management (CoffeeMaker), and payment processing (MoneyMachine). The main module ties everything together to allow users to order drinks, check resource levels, view profit reports, and process payments until the machine is turned off.

## Features

- **Modular Design:** Organized into separate modules for menu management, resource handling, and money transactions.

- **Multiple Drink Options:** Order popular drinks such as latte, espresso, and cappuccino, each with specific ingredient requirements and pricing.

- **Resource Management:** Automatically checks if sufficient resources (water, milk, coffee) are available before processing an order.

- **Coin Processing:** Handles coin transactions, calculates change, updates profit, and refunds insufficient payments.

- **Reporting:** Provides reports on current ingredient levels and total profit.

- **Interactive Interface:** Continuously prompts for user input, supporting commands like "report" and "off" to display status or shut down the machine.

## Installation

### Prerequisites

- **Python 3.x:** Ensure that Python 3 is installed on your system. You can download it from [Python's offical website](python.org).

### How to Run

1. **Download the Code:** Clone the repository or ensure you have all the following files in the same directory:

   - `coffee_machine.py` (Main module)

   - `coffee_maker.py` (Handles ingredient resources and coffee preparation)

   - `menu.py` (Manages available drink options)

   - `money_machine.py` (Processes coin transactions and tracks profit)

2. **Open Terminal/Command Prompt:** Navigate to the directory containing the file.

3. **Run the program:** Execute the following command:

    ```bash
    python3 coffee_machine.py
    ```

4. **Follow the Prompts:**
   - **Order a Drink:** Type `espresso`, `latte`, or `cappuccino` when prompted to purchase a drink.

   - **Check Resources:** Enter `report` to display the current levels of ingredients and money.

   - **Turn Off the Machine:** Enter `off` to shut down the simulation.

   - **Payment Process:** Follow the prompts to insert coins. The machine will process your coins, return change if necessary, and prepare your drink if sufficient resources are available.


## Demo
![Coffee Machine Simulator Demo](https://i.imgur.com/giCAAXt.gif)
[Coffee Machine Simulator Demo](https://i.imgur.com/giCAAXt.gif)

## License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).


## Authors

- Ivis Perdomo [@ivyper](https://www.github.com/ivyper)


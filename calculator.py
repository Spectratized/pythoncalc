"""
Simple CLI Calculator in Python.

Provides core mathematical operations with error handling and an interactive CLI.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference between two numbers (a - b)."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    Return the quotient of two numbers (a / b).

    Raises:
        ValueError: If division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a: Number, b: Number) -> Number:
    """Return a raised to the power of b (a ** b)."""
    return a ** b


def modulus(a: Number, b: Number) -> Number:
    """
    Return the remainder of dividing a by b (a % b).

    Raises:
        ValueError: If modulo by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot perform modulo by zero.")
    return a % b


def get_number(prompt: str) -> float:
    """Prompt the user for a valid number, repeating until valid input is given."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")


def display_menu() -> None:
    """Display the calculator menu options."""
    print("\n" + "=" * 30)
    print("      PYTHON CALCULATOR      ")
    print("=" * 30)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exponentiation (^)")
    print("6. Modulus (%)")
    print("7. Exit")
    print("=" * 30)


def main() -> None:
    """Main loop for the interactive calculator."""
    operations = {
        "1": ("Addition", add, "+"),
        "2": ("Subtraction", subtract, "-"),
        "3": ("Multiplication", multiply, "*"),
        "4": ("Division", divide, "/"),
        "5": ("Exponentiation", power, "^"),
        "6": ("Modulus", modulus, "%"),
    }

    print("Welcome to Python Calculator!")

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "7":
            print("\nThank you for using Python Calculator. Goodbye!\n")
            break

        if choice not in operations:
            print("Invalid choice. Please select a number from 1 to 7.")
            continue

        name, func, symbol = operations[choice]
        print(f"\nSelected: {name}")

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            result = func(num1, num2)
            # Format clean integers without trailing '.0' if applicable
            formatted_res = int(result) if isinstance(result, float) and result.is_integer() else result
            print(f"\nResult: {num1} {symbol} {num2} = {formatted_res}")
        except ValueError as err:
            print(f"\nError: {err}")


if __name__ == "__main__":
    main()

"""
The Crash-Proof Input Tool
Practices: while True loops, try/except, input validation
"""

def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


result = get_valid_number("Enter a number: ")
print("You entered:", result)

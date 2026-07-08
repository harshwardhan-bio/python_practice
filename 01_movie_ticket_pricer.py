"""
Movie Ticket Pricer
Practices: input(), type conversion, if/elif/else conditions
"""

A = input("Enter your age: ")
Age = int(A)

if 0 <= Age <= 12:
    print("Your ticket cost is Rs 100.")
elif 12 < Age <= 60:
    print("Your ticket cost is Rs 250.")
else:
    print("Your ticket cost is Rs 150.")

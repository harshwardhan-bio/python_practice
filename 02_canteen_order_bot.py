"""
SRM Canteen Order Bot
Practices: input(), string methods, if/elif/else conditions
"""

Order = input("What would you like to order?\n1. Paneer Pizza\n2. Masala Dosa\n3. Coffee\n")
type = Order.title()

if type == "Paneer Pizza":
    print("Your order is Paneer Pizza and the cost is Rs 180.")
elif type == "Masala Dosa":
    print("Your order is Masala Dosa and the cost is Rs 80.")
elif type == "Coffee":
    print("Your order is Coffee and the cost is Rs 40.")
else:
    print("Sorry, we don't have that item on the menu.")

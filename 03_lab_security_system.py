"""
Biotech Lab Security System
Practices: input(), string methods, compound conditions (and)
"""

User = input("Is your ID badge valid? (yes/no) ")
User2 = input("Are you wearing your safety goggles? (yes/no) ")

User_for = User.lower()
User_two = User2.lower()

if User_for == "yes" and User_two == "yes":
    print("Access granted. Welcome to the lab.")
elif User_for == "yes" and User_two == "no":
    print("Access denied. Please wear your safety goggles.")
else:
    print("Access denied.")

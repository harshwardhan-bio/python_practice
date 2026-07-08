"""
The Boss Fight
Practices: while loops, decrementing values
"""

boss_health = 100

while boss_health > 0:
    boss_health -= 25
    print(f"Boss health: {boss_health}")

print("Congratulations! You have defeated the boss!")

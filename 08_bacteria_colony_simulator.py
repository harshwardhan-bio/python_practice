"""
Bacteria Colony Simulator
Practices: while True loops, break, exponential growth simulation
"""

Bacteria = 10
Hour = 0
Capacity_limit = int(input("Enter the capacity limit of the petri dish: "))

while True:
    Bacteria *= 2
    Hour += 1
    if Bacteria >= Capacity_limit:
        break

print(f"The petri dish will reach its capacity limit in {Hour} hours with {Bacteria} bacteria.")

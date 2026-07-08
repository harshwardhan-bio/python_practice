"""
Small Cap SIP Tracker
Practices: for loops, range(), f-strings, accumulator pattern
"""

total_investment = 0

for month in range(1, 7):
    amount = 2000
    total_investment += amount
    print(f"Month {month}: Total Investment = Rs {total_investment}")

print(f"Total amount invested over 6 months: Rs {total_investment}")

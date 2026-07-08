"""
The Multi-Error Concentration Calculator
Practices: try/except/finally, multiple exception types
"""

def calculate_molarity(moles, volume):
    try:
        moles = float(moles)
        volume = float(volume)
        concentration = moles / volume
        return concentration
    except ValueError:
        print("Error: Please enter valid numeric values for moles and volume.")
    except ZeroDivisionError:
        print("Error: Volume cannot be zero.")
    finally:
        print("Calculation attempt completed.")


result = calculate_molarity(5, 2)
print(result)

'''
# Adding two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Output
print(f"The answer is {num1 + num2}")

# Core Data types
# str : String/Text - "Hello", "aofhf*&^Ad"
# int : Integers/Whole Numbers - 3, -1, 6
# float : Decimal Numbers - 5.23, 6.1
# bool : Boolean/True or False

# Type casting - Changing one data type to another

'''

# Calculating a tip

bill = float(input("Enter the bill amount: R "))
tip = 0.15

val_tip = bill * tip
total_cost = bill + val_tip

print(f"Here is the tip: R {val_tip}")
print(f"Here is the tip: R {round(val_tip, 2)} rounded")
print("  ")
print(f"Here is the total cost: R {total_cost}")
print(f"Here is the total cost: R {round(total_cost, 2)} rounded")
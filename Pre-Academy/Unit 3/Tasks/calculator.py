# Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Output
# Simple Operations
print("============================================")
print("BASIC OPERATIONS")
print("============================================")
print(f"Addition : {round(num1 + num2, 2)}")
print(f"Subtraction : {round(num1 - num2, 2)}")
print(f"Multipication : {round(num1 * num2, 2)}")

if num2 == 0:
    print("Division : Cannot divide by zero")
else:
    print(f"Division : {round(num1 / num2, 2)}")

print(" ")
print("============================================")
print("ADVANCED OPERATIONS")
print("============================================")

# Advanced Operations

if num2 == 0:
    print("Floor Division : Cannot divide by zero")
    print("Modulus : Cannot divide by zero")
else:
    print(f"Floor Division : {round(num1 // num2, 2)}")
    print(f"Modulus : {round(num1 % num2, 2)}")

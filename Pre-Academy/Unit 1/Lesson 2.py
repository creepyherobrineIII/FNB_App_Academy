# Playing around with variables

int_var = 33
bool_var = False
float_var = 99.2875

print(f'''Integer: {int_var}
Boolean: {bool_var}
Float: {float_var}''')

# Type Conversion
print("\n")
birth_year = int(input("Enter your birth year:"))
age = 2026 - birth_year
print(f"You are {age} years old")

# Calculator exercise
firstNum = float(input("First: "))
secondNum = float(input("Second: "))

print(f"Sum: {firstNum + secondNum}")
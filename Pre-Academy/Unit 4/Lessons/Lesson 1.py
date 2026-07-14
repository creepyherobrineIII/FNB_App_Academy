# Basic if/else statement script

age = int(input("Enter your age: "))
section_pass = input("Do you have a VIP ticket? (yes/ no): ")

if age >= 18 and section_pass.lower() == "yes":
    print("Access granted to the VIP section!")
elif age >= 18:
    print("Access granted to the general section!")
else:
    print("Access denied")


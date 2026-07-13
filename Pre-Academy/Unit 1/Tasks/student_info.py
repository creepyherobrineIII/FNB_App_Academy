first_name = input("Enter your first name: ")
last_name = input("Enter your surname: ")
age = int(input("Age: "))
fav_num  = float(input("Favourite Number: "))

full_name = first_name + ' ' + last_name

print(f'Welcome, {full_name.title()}')
print(full_name.upper())
print(age * 12)
print(round(fav_num, 2))
print(f"{type(full_name)}, {type(age)}, {type(fav_num)}")

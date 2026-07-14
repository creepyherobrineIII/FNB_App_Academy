# Input
kms_driving = float(input("How many kilometers do you plan on driving?: "))
price_per_litre = float(input("What is the current price per litre?: R"))

# Calculations
litres_needed = kms_driving / 10

total_cost = litres_needed * price_per_litre
# Output
print(" ")
print(f"The total cost of petrol: R {round(total_cost, 2)}")
# Exercise
weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
convertedWeight = 0

if unit.upper() == "K":
    convertedWeight = weight * 2.2
    print(f"Weight in Lbs: {convertedWeight}")
else:
    convertedWeight = weight / 2.2
    print(f"Weight in Kg: {convertedWeight}")
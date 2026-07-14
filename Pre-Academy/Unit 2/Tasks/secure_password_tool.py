# Input
password = input("Enter your secret password: ").strip()

# String manipulation with indexing
firstLetter = password[0]
lastLetter = password[-1]

#Output
print(f"Here is a hint for your password: It starts with {firstLetter.upper()} and ends with {lastLetter.upper()}")
# Lists 

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)

# Indexing in a list
print(names[0], names[-2])

# Changing values
names[0] = "Jon"

# Showing a range of values
print(names[0:3]) #Excluding the last value

# List methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # Adding value to list
print(numbers)
numbers.insert(3, 8) # Inserting values into list
print(numbers)
numbers.remove(8) # Removes a value in the list
print(numbers)
print(3 in numbers) # Checks if a value is in a list
#numbers.clear() # Removes all values in the list
#print(numbers)
# Data Collection 
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
bio = input("Enter a short description of yourself: ").strip()

# Manipulating strings
editedBio = bio.replace("I am", "I'm")
full_name = f"{first_name} {last_name}"
# Username creation
username = first_name[0].lower() + last_name.lower()

# Output
print(f"Username: {username}")
print(f"Full Name: {full_name.title()}")
print(f"Bio: {editedBio}\nNumber of characterss in the bio: {len(editedBio)}")

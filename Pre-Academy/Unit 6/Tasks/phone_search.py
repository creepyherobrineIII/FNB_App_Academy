contacts = {'Vanessa': '0837221259', 
     'Bobby': '0147823396', 
     'Devoe': '0625559081'}

search_name = input("Enter the name of the contact you wish to find: ").title()

found_contact = False

for contact in contacts:
    if contacts.get(search_name) != None:
        print(f"Found! {search_name} phone number is {contacts.get(search_name)}")
        found_contact = True
        break
    else:
        continue
    
if found_contact == False:
    print("Contact not found!")


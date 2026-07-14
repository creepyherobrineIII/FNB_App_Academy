action = 0
contact_list = []

def add_contact():
    contact_name = input("Enter the contact's name: ").title()
    contact_phone = input("Enter the contact's phone number: ")
    contact_email = input("Enter the contact's email address: ")

    contact_dictionary = {'name' : contact_name, 'phone': contact_phone, 'email' : contact_email}
    contact_list.append(contact_dictionary)
    print("=============================")
    print('Contact added to book!')

def search_contact(contName):
    found_cont = False
    for contact in contact_list: 
        if contact['name'] == contName:
            found_cont = True
            return(contact[contName])
    
    if found_cont == False:
        return(None)
    

def delete_contact(contName):
    found_cont = False
    for contact in contact_list: 
        if contact['name'] == contName:
            found_cont = True
            contact_list.remove(contact)
            print("Contact deleted successfully")
            break
    
    if found_cont == False:
        print("Contact could not be found")

def view_all():
    for contact in contact_list:
        print(contact)


while(action != 5):
    action = int(input('''Select an option (1 = Add Contact, 2 = Search contacts, 3 = Delete contact
4 = View All contacts, 5 = Exit program): '''))

    print("=============================")
    if action == 1:
        add_contact()
        print("=============================")
    elif action == 2:
        name_to_search = input("Enter a name to search: ").title()
        print("=============================")
        result = search_contact(name_to_search)
        print(result)
        print("=============================")
    elif action == 3:
        name_to_del = input("Enter a contact's name to delete: ").title()
        print("=============================")
        delete_contact(name_to_del)
        print("=============================")
    elif action == 4:
        view_all()
        print("=============================")
    elif action == 5:
        print("Goodbye!")




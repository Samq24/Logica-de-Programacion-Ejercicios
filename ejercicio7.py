def add_contact(contact_list, name, phone):
    if not phone.isdigit():
        print(f"Warning: The phone number for {name} is invalid. It should contain only digits.")
        return contact_list
    contact_list[name] = phone
    return contact_list

def remove_contact(contact_list, name):
    if name in contact_list:
        del contact_list[name]
    return contact_list

def show_contacts(contact_list):
    for name, phone in contact_list.items():
        print(f"{name}: {phone}")

contacts = {}

[add_contact(contacts, name, phone) for name, phone in [("Luke", "123456789"), ("Leia", "987654321"), ("Han", "456123789"), ("Chewbacca", "GRRR GRR GRRRRRR GR m"), ("Yoda", "987*654")]]

contacts = remove_contact(contacts, "Luke")

show_contacts(contacts)
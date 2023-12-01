contacts = []

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print("Contact added successfully!")

def display_contacts():
    print("\n--- Contacts ---")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['Name']}")

def search_contact():
    search_term = input("Enter the name to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact["Name"].lower()]

    if found_contacts:
        print("\n--- Search Results ---")
        for contact in found_contacts:
            print_contact(contact)
    else:
        print("Contact not found.")

def update_contact():
    display_contacts()
    try:
        index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print("\nEnter new details:")
            contact["Name"] = input("Name: ")
            contact["Phone"] = input("Phone number: ")
            contact["Email"] = input("Email address: ")
            contact["Address"] = input("Address: ")
            print("Contact updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_contact():
    display_contacts()
    try:
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            del contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def print_contact(contact):
    print("\n--- Contact Details ---")
    print(f"Name: {contact['Name']}")
    print(f"Phone: {contact['Phone']}")
    print(f"Email: {contact['Email']}")
    print(f"Address: {contact['Address']}")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

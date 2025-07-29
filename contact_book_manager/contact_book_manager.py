# Contact Book Manager

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    number = input("Enter phone number: ").strip()
    
    if name in contacts:
        print("Contact already exists. Updating number.")
    contacts[name] = number
    print(f"Contact '{name}' saved successfully.\n")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("📒 Contact List:")
    for name, number in contacts.items():
        print(f"Name: {name}, Number: {number}")
    print()


def search_contact(contacts):
    search_name = input("Enter name to search: ").strip()
    if search_name in contacts:
        print(f"Found: {search_name} → {contacts[search_name]}\n")
    else:
        print(f"Contact '{search_name}' not found.\n")


def contact_book():
    contacts = {}
    while True:
        print("------ Contact Book Menu ------")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.\n")


if __name__ == "__main__":
    contact_book()

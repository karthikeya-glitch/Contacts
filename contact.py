class ContactBook:
    def __init__(self):
        self.contacts = []  # List of (name, phone) tuples

    def add_contact(self, name, phone):
        self.contacts.append((name, phone))
        print(f"Contact {name} added")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for idx, (name, phone) in enumerate(self.contacts):
                print(f"{idx}: {name} - {phone}")

    def search_contact(self, name):
        # Partial, case-insensitive match logic
        found = False
        for idx, (contact_name, phone) in enumerate(self.contacts):
            if name.lower() in contact_name.lower():
                print(f"Found: {contact_name} - {phone}")
                found = True
        if not found:
            print("Contact not found")

    def delete_contact(self, idx):
        # Index bounds checking
        if 0 <= idx < len(self.contacts):
            del self.contacts[idx]
            print("Contact deleted")
        else:
            print("Error: Invalid index. No contact deleted.")

    def update_contact(self, idx, name, phone):
        # Index bounds checking and correct update logic
        if 0 <= idx < len(self.contacts):
            self.contacts[idx] = (name, phone)
            print("Contact updated")
        else:
            print("Error: Invalid index. No contact updated.")

def main():
    book = ContactBook()
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Update Contact\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            book.add_contact(name, phone)
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            book.search_contact(name)
        elif choice == "4":
            try:
                idx = int(input("Enter contact index to delete: "))
                book.delete_contact(idx)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == "5":
            try:
                idx = int(input("Enter contact index to update: "))
                name = input("Enter new name: ")
                phone = input("Enter new phone: ")
                book.update_contact(idx, name, phone)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

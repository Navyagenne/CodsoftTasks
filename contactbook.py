class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"Contact {idx}:\n{contact}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not results:
            print("No contacts found with that search term.")
        else:
            for contact in results:
                print(contact)

    def update_contact(self, search_term):
        for contact in self.contacts:
            if contact.name == search_term or contact.phone == search_term:
                print("Contact found:")
                print(contact)
                name = input("Enter new name (leave blank to keep current): ") or contact.name
                phone = input("Enter new phone (leave blank to keep current): ") or contact.phone
                email = input("Enter new email (leave blank to keep current): ") or contact.email
                address = input("Enter new address (leave blank to keep current): ") or contact.address
                contact.name, contact.phone, contact.email, contact.address = name, phone, email, address
                print("Contact updated successfully.")
                return
        print("No contact found with that name or phone number.")

    def delete_contact(self, search_term):
        for i, contact in enumerate(self.contacts):
            if contact.name == search_term or contact.phone == search_term:
                print("Contact found and deleted:")
                print(contact)
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("No contact found with that name or phone number.")


def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == "4":
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)

        elif choice == "5":
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

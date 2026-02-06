
# Mini Project 1: Contact Book Application


# Dictionary to store contacts
contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1. Add a new contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print("Contact added successfully!")

    # 2. Update contact details
    elif choice == "2":
        name = input("Enter Name to update: ")

        if name in contacts:
            phone = input("Enter new Phone Number: ")
            email = input("Enter new Email: ")

            contacts[name]["phone"] = phone
            contacts[name]["email"] = email
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # 3. Delete a contact by name
    elif choice == "3":
        name = input("Enter Name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # 4. Search for a contact by name
    elif choice == "4":
        name = input("Enter Name to search: ")

        if name in contacts:
            print("Name :", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact not found!")

    # 5. Display all contacts
    elif choice == "5":
        if not contacts:
            print("No contacts available.")
        else:
            print("\nContact Book")
            print("-----------------------")
            for name, details in contacts.items():
                print("Name :", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("-----------------------")

    # 6. Exit the application
    elif choice == "6":
        print("Exiting Contact Book Application.")
        break

    else:
        print("Invalid choice! Please try again.")

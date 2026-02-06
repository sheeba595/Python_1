# ----------------------------------
# Library Book Management System
# ----------------------------------

library = {}

while True:
    print("\n1. Add Book")
    print("2. Borrow / Return Book")
    print("3. Remove Book")
    print("4. View All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1. Add a new book
    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        copies = int(input("Enter Number of Copies: "))

        library[book_id] = {
            "title": title,
            "author": author,
            "copies": copies
        }
        print("Book added successfully!")

    # 2. Update book availability (borrow / return)
    elif choice == "2":
        book_id = input("Enter Book ID: ")

        if book_id in library:
            print("1. Borrow Book")
            print("2. Return Book")
            action = input("Choose action: ")

            if action == "1":
                if library[book_id]["copies"] > 0:
                    library[book_id]["copies"] -= 1
                    print("Book borrowed successfully!")
                else:
                    print("No copies available!")

            elif action == "2":
                library[book_id]["copies"] += 1
                print("Book returned successfully!")
            else:
                print("Invalid action!")

        else:
            print("Book not found!")

    # 3. Remove a book
    elif choice == "3":
        book_id = input("Enter Book ID to remove: ")

        if book_id in library:
            del library[book_id]
            print("Book removed successfully!")
        else:
            print("Book not found!")

    # 4. List all available books
    elif choice == "4":
        if not library:
            print("Library is empty.")
        else:
            print("\nAvailable Books")
            print("--------------------------------")
            for book_id, details in library.items():
                print("Book ID :", book_id)
                print("Title   :", details["title"])
                print("Author  :", details["author"])
                print("Copies  :", details["copies"])
                print("--------------------------------")

    # 5. Exit
    elif choice == "5":
        print("Exiting Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")

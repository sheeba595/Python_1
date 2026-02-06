# ----------------------------------
# Mini Project 1: Student Management System (Using Lists)
# ----------------------------------

# List to store student names
students = []

while True:
    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Name")
    print("4. Show All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add a new student
    if choice == "1":
        name = input("Enter Student Name: ")
        students.append(name)
        print("Student added successfully!")

    # Remove a student
    elif choice == "2":
        name = input("Enter Student Name to remove: ")
        if name in students:
            students.remove(name)
            print("Student removed successfully!")
        else:
            print("Student not found!")

    # Update a student name
    elif choice == "3":
        old_name = input("Enter existing student name: ")
        if old_name in students:
            new_name = input("Enter new student name: ")
            index = students.index(old_name)
            students[index] = new_name
            print("Student name updated successfully!")
        else:
            print("Student not found!")

    # Show all students
    elif choice == "4":
        print("Student List:", students)

    # Exit the system
    elif choice == "5":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice! Please try again.")

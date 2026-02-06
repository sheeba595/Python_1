# Mini Project 1: Student Grade Tracker 

# Initialize an empty list to store student data 
students = [] 
# Function to add a student 
def add_student(name, grade): 

    students.append([name, grade]) 
    print(f"Student {name} with grade {grade} added!") 
# Function to update a grade 
def update_grade(name, new_grade): 
    for student in students: 
        if student[0] == name: 
            student[1] = new_grade 
            print(f"Grade for {name} updated to {new_grade}") 
            return 
    print("Student not found!") 
# Function to remove a student 
def remove_student(name): 
    global students 
    students = [student for student in students if student[0] != name] 
    print(f"Student {name} removed!") 
# Function to display all students 
def display_students(): 
    print("\nStudent List:") 
    for student in students: 
        print(f"{student[0]}: {student[1]}") 
# Menu-driven program 
while True: 
    print("\n1. Add Student\n2. Update Grade\n3. Remove Student\n4. Display Students\n5. Exit") 
    choice = int(input("Enter your choice: ")) 
    if choice == 1: 
        name = input("Enter student name: ") 
        grade = input("Enter grade: ") 
        add_student(name, grade) 
    elif choice == 2: 
        name = input("Enter student name: ") 
        new_grade = input("Enter new grade: ") 

        update_grade(name, new_grade) 
    elif choice == 3: 
        name = input("Enter student name to remove: ") 
        remove_student(name) 
    elif choice == 4: 
        display_students() 
    elif choice == 5: 
        print("Exiting program...") 
        break 
    else: 
        print("Invalid choice! Please try again.")
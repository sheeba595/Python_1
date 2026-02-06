students = []

while True:
    print("1.Add Student  2.View Students  3.Average Marks  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Student name: ")
        marks = int(input("Marks: "))
        students.append([name, marks])

    elif choice == 2:
        for s in students:
            print(s)

    elif choice == 3:
        total = sum(s[1] for s in students)
        print("Average:", total / len(students))

    elif choice == 4:
        break

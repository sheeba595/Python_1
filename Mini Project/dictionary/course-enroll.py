# ----------------------------------
# Student Course Enrollment System
# ----------------------------------

# 1. Available courses
available_courses = {
    "Python",
    "Java",
    "Web Development",
    "Data Science",
    "Machine Learning"
}

# Student enrolled courses
student_courses = set()

while True:
    print("\nAvailable Courses:", available_courses)
    print("1. Enroll in a Course")
    print("2. Remove a Course")
    print("3. View Enrolled Courses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # 2. Enroll in course
    if choice == "1":
        course = input("Enter course name to enroll: ")

        if course in available_courses:
            student_courses.add(course)
            print("Successfully enrolled in", course)
        else:
            print("Course not found!")

    # 4. Remove a course
    elif choice == "2":
        course = input("Enter course name to remove: ")

        if course in student_courses:
            student_courses.remove(course)
            print("Course removed successfully!")
        else:
            print("You are not enrolled in this course!")

    # View enrolled courses
    elif choice == "3":
        if not student_courses:
            print("No courses enrolled yet.")
        else:
            print("Enrolled Courses:")
            for c in student_courses:
                print("-", c)

    # 5. Exit and show final list
    elif choice == "4":
        print("\nFinal Enrolled Courses:")
        for c in student_courses:
            print("-", c)
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Try again.")

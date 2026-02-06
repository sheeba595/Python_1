from functools import reduce

 
# Mini Project 1: Student Grade Management System
 

# Create a function calculate_average(*args) that takes multiple subject marks
# and returns the average score.
def calculate_average(*args):
    return sum(args) / len(args)


students_marks = [
    ("Sheeba", [95, 88, 92]),
    ("Arun", [78, 74, 80]),
    ("Meena", [60, 65, 58]),
    ("Rahul", [85, 90, 82])
]


def get_grade(avg):
    return (
        "A" if avg >= 90 else
        "B" if avg >= 80 else
        "C" if avg >= 70 else
        "F"
    )


students = []

for name, marks in students_marks:
    avg = calculate_average(*marks)
    grade = get_grade(avg)
    student = {
        "name": name,
        "average": avg,
        "grade": grade
    }
    students.append(student)


passed_students = list(filter(lambda s: s["grade"] != "F", students))


highest_score = reduce(
    lambda a, b: a if a > b else b,
    [student["average"] for student in students]
)


def print_students_recursive(students, n, index=0):
    if index == n or index >= len(students):
        return
    print(students[index])
    print_students_recursive(students, n, index + 1)


 
print("All Students:")
for s in students:
    print(s)

print("\nPassed Students:")
for s in passed_students:
    print(s)

print("\nHighest Average Score:", highest_score)

print("\nFirst 3 Students (Using Recursion):")
print_students_recursive(students, 3)

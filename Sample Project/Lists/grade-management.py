# Mini Project 3: Student Grades Management using Tuples
# Tuple storing student names and grades 
students = ("Alice", "Bob", "Charlie", "David") 
grades = (85, 92, 78, 90) 
# Display all students and grades 
print("Student Grades:") 
for i in range(len(students)): 
    print(f"{students[i]}: {grades[i]}") 
# Finding highest, lowest, and average grade 
print("\nStatistics:") 
print(f"Highest Grade: {max(grades)}") 
print(f"Lowest Grade: {min(grades)}") 
print(f"Average Grade: {sum(grades) / len(grades):.2f}") 
# Accessing a student's grade 
index = students.index("Charlie") 
print(f"\nCharlie's Grade: {grades[index]}")
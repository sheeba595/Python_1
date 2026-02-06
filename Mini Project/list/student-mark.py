# ----------------------------------
# Mini Project 3: Student Marks Analyzer using Tuples
# ----------------------------------

# Create a tuple containing marks of 5 subjects for a student
marks = (85, 90, 78, 88, 92)

print("Student Marks:", marks)

# Calculate total marks using sum()
total_marks = sum(marks)

# Find highest marks using max()
highest_marks = max(marks)

# Find lowest marks using min()
lowest_marks = min(marks)

# Calculate average marks
average_marks = total_marks / len(marks)

print("Total Marks:", total_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", average_marks)


# Convert the tuple to a list, modify one subject mark, and convert it back to a tuple
marks_list = list(marks)          # Tuple to List
marks_list[2] = 80                # Modify one subject mark
marks = tuple(marks_list)         # List back to Tuple

print("Updated Marks Tuple:", marks)

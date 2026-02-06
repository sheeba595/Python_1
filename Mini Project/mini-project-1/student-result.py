name = input("Enter student name: ")
marks = []

for i in range(1, 6):
    m = int(input(f"Enter mark {i}: "))
    marks.append(m)

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)

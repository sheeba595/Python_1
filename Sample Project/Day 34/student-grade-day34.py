students = { 
    "John": 85, 

    "Emma": 92, 
    "Liam": 78, 
    "Olivia": -1,  # Absent 
    "Sophia": 90, 
    "James": 65 
} 
total_marks = 0 
count = 0 
print("Student Rankings:") 
for index, (name, marks) in enumerate(students.items(), start=1): 
    if marks == -1:   
        continue  # Skip absent students 
    total_marks += marks 
    count += 1 
    print(f"{index}. {name} - {marks} marks") 
avg_marks = total_marks / count if count > 0 else 0 
print(f"\nClass Average Marks: {avg_marks}") 
# Identify top performers 
print("\nTop Performers:") 
for name, marks in students.items(): 
    if marks >= 80: 
        print(f"🏆 {name} - {marks} marks")
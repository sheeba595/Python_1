# Mini Project 1: Student Profile Card Generator 
# Project Description: 
# Create a Python program that takes a student's name, age, course, and university 
# name as input and generates a formatted profile card. 
# Taking input from the user 
name = input("Enter Student Name: ").strip().title() 
age = input("Enter Age: ").strip() 
course = input("Enter Course Name: ").strip().title() 
university = input("Enter University Name: ").strip().title() 
# Generating formatted profile 
profile = f""" 
�
� Student Profile 🎓 --------------------- 
Name      : {name} 
Age       : {age} 
Course    : {course} 
University: {university} --------------------- 
Note: Keep working hard and learning new things!  
""" 
# Printing the formatted student profile 
print(profile)
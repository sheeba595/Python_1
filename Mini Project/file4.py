# This project will take a student's name, class, marks in three subjects, calculate 
# the total and percentage, and display a formatted report card. 
stud_name=input("Enter name: ")
tamil=input("Enter marks for Tamil")
english=input("Enter marks for English")
science=input("Enter marks for Science")
total=tamil+english+science
percentage=(total/300)*100
print("****Student Report Card****")
print(f"""
      Name: {stud_name}
      Tamil: {tamil}
      English: {english}
      Science: {science}
      Total: {total}
      Percentage: {percentage}""")

# This project will take an employee's name, basic salary, and allowances, calculate 
# deductions (tax), and display the final salary slip.
employee_name=input("Enter employee name: ")
basic_salary=input("Enter basic salary: ")
allowance=input("Enter allowances: ")
tax=basic_salary*0.10
final_salary=basic_salary+allowance-tax
print(f"""Name of the employee: {employee_name}
            Basic Salary: {basic_salary}
            Allowance: {allowance}
            Final Salary: {final_salary}
      """)


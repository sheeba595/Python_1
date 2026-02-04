# Mini Project 3: To-Do List Manager (Using while, continue, break, else) 
# Task: 
# Create a To-Do List Manager where users can: 
#  Add tasks (User enters a task to add). 
#  View tasks (Display all tasks). 
#  Remove tasks (User enters the task number to delete it). 
#  Exit the program when the user types "exit".

tasks=[]
while True:
    print("""1.Add Tasks    2.View Tasks    3.Remove Task    4.Exit Task""")
    user=input("Enter your operation: ")
    if user=="4" or user.lower()=="exit":
        print(f"Exited!!")
        break
    elif(user=="1"):
        add=input("Add task: ")
        tasks.append(add)
        print(f"Task added successfully!")
        continue
    elif user=="2":
        if len(tasks)==0:
            print(f"No tasks found!!")
            continue
        else:
            for index,task in enumerate(tasks,start=1):
                print(f"{index}=>{task}")
        continue
    elif (user=="3"):
        if not tasks:
            print(f"No task found")
            continue
        else:
             for index,task in enumerate(tasks,start=1):
                print(f"{index}=>{task}")
             num=int (input("Enter task number to remove: "))
             if 1<=num<=len(tasks):
                removed=tasks.pop(num-1)
                print("Task removed successfully!!")
                continue
             else:
                print("Invalid task number")
                continue
           
    else:
        print("Invalid choice! Try again.")
        continue
 
                
           
    
                
        
    
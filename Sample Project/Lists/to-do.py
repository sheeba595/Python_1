# Mini Project 2: To-Do List Manager 

# Initialize an empty to-do list 
todo_list = [] 
# Function to add a task 
def add_task(task): 
    todo_list.append(task) 
    print(f"Task '{task}' added!") 
# Function to remove a task 
def remove_task(task): 

    if task in todo_list: 
        todo_list.remove(task) 
        print(f"Task '{task}' removed!") 
    else: 
        print("Task not found!") 
# Function to display tasks 
def display_tasks(): 
    if not todo_list: 
        print("\nNo tasks to show!") 
    else: 
        print("\nTo-Do List:") 
        for index, task in enumerate(todo_list, start=1): 
            print(f"{index}. {task}") 
# Menu-driven program 
while True: 
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit") 
    choice = int(input("Enter your choice: ")) 
    if choice == 1: 
        task = input("Enter task: ") 
        add_task(task) 
    elif choice == 2: 
        task = input("Enter task to remove: ") 
        remove_task(task) 
    elif choice == 3: 
        display_tasks() 
    elif choice == 4: 
        print("Exiting program...") 
        break 
    else: 
        print("Invalid choice! Please try again.") 
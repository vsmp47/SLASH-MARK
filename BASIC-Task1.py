# Initiating an empty list to hold tasks
my_tasks = []

# Function to show the to-do list
def show_tasks():
    if not my_tasks:
        print("Your to-do list is currently empty.")
    else:
        print("Tasks to be Completed:")
        for i, task in enumerate(my_tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")

# Function to include a new task in the to-do list
def add_new_task(task_name):
    task = {"task": task_name, "completed": False}
    my_tasks.append(task)
    print(f"New task '{task_name}' has been added to your to-do list.")

# Function to indicate a task as done
def mark_as_done(task_number):
    if 1 <= task_number <= len(my_tasks):
        my_tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} has been marked as completed.")
    else:
        print("The task number provided is invalid. Please provide a valid task number.")

# Function to eliminate a task from the to-do list
def remove_specific_task(task_number):
    if 1 <= task_number <= len(my_tasks):
        removed_task = my_tasks.pop(task_number - 1)
        print(f"The task '{removed_task['task']}' has been removed from your to-do list.")
    else:
        print("The task number provided is invalid. Please provide a valid task number.")

# Main program execution loop
while True:
    print("\nOptions:")
    print("1. View to-do list")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")
    choice = input("Please enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task_name = input("Enter the new task: ")
        add_new_task(task_name)
    elif choice == '3':
        show_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_as_done(task_number)
    elif choice == '4':
        show_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_specific_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please select a valid option.")

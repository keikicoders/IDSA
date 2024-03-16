task_list = []
task = ''
new_task = ''

while True:
    print("\nOptions:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(task_list)
    elif choice == '2':
        new_task = input("Enter the new task: ")
        task_list.append(new_task)
    elif choice == '3':
        while task not in task_list:
            task = input("Enter the task index to remove: ")
            if task not in task_list:
                print("Task not found. Try again.")
            else:
                task_list.remove(task)
                break
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

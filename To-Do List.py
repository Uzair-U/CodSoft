# Function to add a task to the list
def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")  # Provide feedback to the user

# Function to remove a task from the list
def remove_task(tasks, task):
    # Check if the task exists in the list
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")  # Provide feedback to the user
    else:
        print("Task not found in the list.")  # Notify the user if the task is not found

# Function to display all tasks in the list
def display_tasks(tasks):
    # Check if there are tasks in the list
    if tasks:
        print("Your To-Do List:")  # Print a header
        # Iterate over each task and print it
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")  # Notify the user if the list is empty


# Function to run the To-Do List application
def main():
    tasks = []  # Initialize an empty list to store tasks

    # Main loop to interact with the user
    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")  # Prompt the user for input

        # Check the user's choice and perform the corresponding action
        if choice == '1':
            task = input("Enter the task you would like to add: ")  # Prompt the user to enter a task
            add_task(tasks, task)  # Call the add_task function
        elif choice == '2':
            task = input("Enter the task you would like to remove: ")  # Prompt the user to enter a task to remove
            remove_task(tasks, task)  # Call the remove_task function
        elif choice == '3':
            display_tasks(tasks)  # Call the display_tasks function
        elif choice == '4':
            print("Exiting the application. Goodbye!")  # Print a goodbye message
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")  # Notify the user for invalid input


# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function to start the application

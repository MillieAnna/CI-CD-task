tasks = []

def show_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks yet.")

def add_task():

    task = "Task from branch2"  # Simulated task input

    tasks.append(task)
    print(f"Added task: {task}")

def main():
    # Simulate user input for CI
    choices = ["1", "2", "3"]  # Predefined choices for testing
    for choice in choices:
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

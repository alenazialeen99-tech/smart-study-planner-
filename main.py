
tasks = []

def add_task():
    name = input("Enter task name: ")
    subject = input("Enter subject: ")
    hours = float(input("Enter study hours: "))

    task = {
        "name": name,
        "subject": subject,
        "hours": hours,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} | "
              f"{task['subject']} | "
              f"{task['hours']} hours | {status}")

def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n=== Smart Study Planner ===")
        print("1. Add a study task")
        print("2. View all tasks")
        print("3. Complete a task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Good luck with your studies!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)

def show_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
while True:
    choice = input("Choose: add/remove/show/quit: ").lower()
    if choice == "add":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "remove":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "show":
        show_tasks()
    elif choice == "quit":
        break
    else:
        print("Invalid choice!")

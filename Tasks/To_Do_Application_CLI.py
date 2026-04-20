import datetime
import json
import os

tasks = []
FNAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FNAME):
        return
    with open(FNAME, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                tasks.append(json.loads(line))
            except json.JSONDecodeError:
                continue

def add_task():
    if tasks:
        task_id = max(task['id'] for task in tasks) + 1
    else:
        task_id = 1
    title = input("Enter the task title: ")
    raw_status = input("Enter the task status (1-Not Done, 2-Pending): ").strip()

    if raw_status == '1':
        status = "Not Done"
    elif raw_status == '2':
        status = "Pending"
    else:
        print("Invalid status choice, defaulting to 'Not Done'.")
        status = "Not Done"

    new_task = {
        "id": task_id,
        "title": title,
        "status": status,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)                     
    with open(FNAME, "a") as file:            
        file.write(json.dumps(new_task) + "\n")
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Created At: {task['created_at']}")

def mark_task_as_done():
    try:
        task_id = int(input("Enter the task ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "Done"
            print("Task marked as done!")
            save_tasks()
            return
    print("Task not found.")

def delete_task():
    try:
        task_id = int(input("Enter the task ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            save_tasks()
            return
    print("Task not found.")

def save_tasks():
    with open(FNAME, "w") as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")

def menu():
    while True:
        print("\nTo-Do Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_as_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
            print("Good Bye")
            break
        else:
            print("Invalid input")

def main():
    load_tasks()   # load once at start
    menu()

if __name__ == "__main__":
    main()

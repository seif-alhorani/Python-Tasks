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

def Add():
    if tasks:
        task_id = max(task['id'] for task in tasks) + 1
    else:
        task_id = 1
    title = input("Enter the task title: ")
    status = input("Enter the task status: ")
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

def View():
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Created At: {task['created_at']}")

def Mark_Task_as_Done():
    task_id = int(input("Enter the task ID: "))
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "Done"
            print("Task marked as done!")
            return
    print("Task not found.")

def Delete():
    task_id = int(input("Enter the task ID: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
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
            Add()
        elif choice == '2':
            View()
        elif choice == '3':
            Mark_Task_as_Done()
        elif choice == '4':
            Delete()
        elif choice == '5':
            save_tasks()
            print("Exiting the application. Goodbye!")
            break

def main():
    load_tasks()   # load once at start
    menu()

if __name__ == "__main__":
    main()

def main():
    while True:
        MainMenu_choice = main_menu()

        if MainMenu_choice == 1:
            task_menu()

        elif MainMenu_choice == 2:
            list_menu()

        else:
            exit()

tasks = []
lists = []

def main_menu():
    MainMenu = ["1. Task", "2. List", "3. Exit"]

    for m in MainMenu:
        print(m)

    while True:
        try:
            MainMode = int(input("Input a number to choose: "))

            if MainMode in [1, 2, 3]:
                return MainMode

            else:
                print("Please choose one of the given numbers")

        except ValueError:
            print("Please input an integer")



def add_new_task(name, due_date = None):
    task = {"name": name, "completed": False, "due_date": due_date}
    tasks.append(task)

    print("New task added:", task)

def mark_task_as_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed")

    else:
        print("Invalid task number.")

def edit_task(index, new_name = None, new_due_date = None):
    if 0 <= index < len(tasks):
        if new_name:
            tasks[index]["name"] = new_name

        elif new_due_date:
            tasks[index]["due_date"] = new_due_date

        print("Task updated")

    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task['name']}' deleted")

    else:
        print("Invalid task number.")

def view_task():
    if not tasks:
        print("No tasks available.")

    else:
        for index, task in enumerate(tasks, start=1):
            completed_status = "✓" if task["completed"] else "✗"
            due_date_info = f"(Due: {task['due_date']})" if task["due_date"] else ""

            print(f"{index}. {task['name']} {due_date_info} - Completed: {completed_status}")

def task_menu():
    while True:
        TaskMenu_choice = [
            "1. Add New Task",
            "2. Mark Task as Completed",
            "3. Edit Task",
            "4. Delete Task",
            "5. View Task",
            "6. Exit"]

        for t in TaskMenu_choice:
            print(t)

        try:
            task_choice = int(input("Input a number to choose: "))

            if task_choice == 1:
                name = input("Enter task name: ")
                due_date = input("Enter due date (optional): ")

                add_new_task(name, due_date)

            elif task_choice == 2:
                index = int(input("Enter task number to mark as completed: ")) - 1

                mark_task_as_completed(index)

            elif task_choice == 3:
                index = int(input("Enter task number to edit: ")) - 1

                new_name = input("Enter new task name (or press Enter to skip): ")
                new_due_date = input("Enter new due date (or press Enter to skip): ")

                edit_task(index, new_name, new_due_date)

            elif task_choice == 4:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)

            elif task_choice == 5:
                view_task()

            elif task_choice == 6:
                break

            else:
                print("Please choose one of the given numbers")

        except ValueError:
            print("Please input an integer")

def add_new_list(name, items = None):
    new_list = {"name": name, "items": items or []}
    lists.append(new_list)

    print(f"List '{name}' added successfully!")

def view_lists():
    if not lists:
        print("No lists available.")

    else:
        for i, lst in enumerate(lists, start = 1):
            print(f"{i}. {lst['name']}")

            if lst["items"]:
                for item in lst["items"]:
                    print(f"   - {item}")

            else:
                print("   (No items in this list)")

def manage_list(index, action, item = None):
    if 0 <= index < len(lists):
        if action == "add" and item:
            lists[index]["items"].append(item)
            print(f"Item '{item}' added to list '{lists[index]['name']}'!")

        elif action == "remove" and item in lists[index]["items"]:
            lists[index]["items"].remove(item)
            print(f"Item '{item}' removed from list '{lists[index]['name']}'!")

        else:
            print("Invalid action or item not found.")

    else:
        print("Invalid list number.")

def delete_list(index):
    if 0 <= index < len(lists):
        removed_list = lists.pop(index)
        print(f"List '{removed_list['name']}' deleted!")

    else:
        print("Invalid list number.")

def list_menu():
    while True:
        ListMenu_choice = [
            "1. Add New List",
            "2. View Lists",
            "3. Manage Lists",
            "4. Delete List",
            "5. Exit"]

        for l in ListMenu_choice:
            print(l)

        try:
            list_choice = int(input("Input a number to choose: "))

            if list_choice == 1:
                name = input("Enter list name: ")
                add_new_list(name)

            elif list_choice == 2:
                view_lists()

            elif list_choice == 3:
                index = int(input("Enter list number to manage: ")) - 1
                action = input("Enter action (add/remove): ")
                item = input("Enter item to add/remove: ")
                manage_list(index, action, item)

            elif list_choice == 4:
                index = int(input("Enter list number to delete: ")) - 1
                delete_list(index)

            elif list_choice == 5:
                break

            else:
                print("Please choose one of the given numbers")

        except ValueError:
            print("Please input an integer")

if __name__ == "__main__":
    main()
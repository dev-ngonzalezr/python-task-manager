from task_manager import TaskManager
from ai_service import create_simple_tasks


def main():
    task_manager = TaskManager()
    print("Welcome to the Task Manager")
    while True:
        print("Main Menu: ")
        print("1. List all tasks")
        print("2. Add a new task")
        print("3. Add a complex task")
        print("4. Remove a task")
        print("5. Complete a task")
        print("6. Exit")
        option_selected = request_user_a_number()
        match option_selected:
            case 1:
                task_manager.list_tasks()
            case 2:
                description = input("Enter a description: ")
                task_manager.add_task(description)
            case 3:
                description = input("Enter a full description: ")
                try:
                    simple_tasks = create_simple_tasks(description)
                    for simple_task in simple_tasks:
                        task_manager.add_task(simple_task)
                except Exception as e:
                    print(e)
            case 4:
                task_id = request_user_a_number("Task id to remove: ")
                task_manager.remove_task(task_id)
            case 5:
                task_id = request_user_a_number("Task id to complete: ")
                task_manager.complete_task(task_id)
            case 6:
                break
            case _:
                print("Invalid option")



def request_user_a_number( prompt="Select an option: "):
    try:
        option_selected = int(input(prompt))
        return option_selected
    except ValueError:
        print("Input must be an integer")
        request_user_a_number(prompt)

if __name__ == "__main__":
    main()
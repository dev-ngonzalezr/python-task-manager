from task import Task
import json

class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def __str__ (self):
        for task in self._tasks:
            print(task)

    def _move_id(self):
        self._next_id = self._next_id + 1

    def add_task(self, description):
        self._tasks.append(Task(self._next_id, description))
        self.save_tasks()
        self._move_id()

    def list_tasks(self):
        self.__str__()

    def remove_task(self, task_id):
        for task in self._tasks:
            if task.get_id() == task_id:
                self._tasks.remove(task)
                print(f"Task {task_id} removed")
                self.save_tasks()
                break

    def complete_task(self, task_id):
        for task in self._tasks:
            if task.get_id() == task_id:
                task.set_completed(True)
                print(f"Task {task_id} completed")
                self.save_tasks()
                break

    def load_tasks(self):
        try:
            with open(self.FILENAME) as json_file:
                data = json.load(json_file)
                self._tasks = [Task(item["id"],item["description"],item["completed"]) for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].get_id() + 1
        except FileNotFoundError:
            print(f"File not found")


    def save_tasks(self):
        with open(self.FILENAME, "w") as json_file:
            json.dump([{"id": task.get_id(), "description": task.get_description(), "completed": task.get_completed()} for task in self._tasks], json_file, indent=4)
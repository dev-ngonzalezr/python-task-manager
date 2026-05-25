import os
import json
import unittest
from task_manager import TaskManager

class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        TaskManager.FILENAME = self.test_file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.manager = TaskManager()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def adds_task_and_persists(self):
        self.manager.add_task("Buy milk")
        self.assertEqual(len(self.manager._tasks), 1)
        self.assertEqual(self.manager._tasks[0].get_description(), "Buy milk")
        with open(self.test_file) as f:
            data = json.load(f)
            self.assertEqual(data[0]["description"], "Buy milk")

    def removes_task_by_id(self):
        self.manager.add_task("Task 1")
        task_id = self.manager._tasks[0].get_id()
        self.manager.remove_task(task_id)
        self.assertEqual(len(self.manager._tasks), 0)

    def completes_task_by_id(self):
        self.manager.add_task("Task 2")
        task_id = self.manager._tasks[0].get_id()
        self.manager.complete_task(task_id)
        self.assertTrue(self.manager._tasks[0].get_completed())

    def loads_tasks_from_file(self):
        tasks = [
            {"id": 1, "description": "A", "completed": False},
            {"id": 2, "description": "B", "completed": True}
        ]
        with open(self.test_file, "w") as f:
            json.dump(tasks, f)
        manager2 = TaskManager()
        self.assertEqual(len(manager2._tasks), 2)
        self.assertEqual(manager2._tasks[1].get_description(), "B")
        self.assertTrue(manager2._tasks[1].get_completed())

    def handles_missing_file_on_load(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        manager2 = TaskManager()
        self.assertEqual(len(manager2._tasks), 0)

    def increments_id_after_add(self):
        self.manager.add_task("First")
        self.manager.add_task("Second")
        self.assertEqual(self.manager._tasks[1].get_id(), self.manager._tasks[0].get_id() + 1)

    def does_nothing_when_removing_nonexistent_id(self):
        self.manager.add_task("Only")
        self.manager.remove_task(999)
        self.assertEqual(len(self.manager._tasks), 1)

    def does_nothing_when_completing_nonexistent_id(self):
        self.manager.add_task("Only")
        self.manager.complete_task(999)
        self.assertFalse(self.manager._tasks[0].get_completed())

if __name__ == "__main__":
    unittest.main()


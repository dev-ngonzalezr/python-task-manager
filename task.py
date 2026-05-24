class Task:
    def __init__(self, task_id, description, completed = False):
        self._id = task_id
        self._description = description
        self._completed = completed

    def __str__ (self):
        status = "V" if self._completed else ""
        return f"[{status}] #{self._id}: {self._description}"

    def get_id(self):
        return self._id

    def get_description(self):
        return self._description

    def get_completed(self):
        return self._completed

    def set_completed(self, completed):
        self._completed = completed


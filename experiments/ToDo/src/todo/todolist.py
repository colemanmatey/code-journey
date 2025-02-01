"""
The ToDoList class
"""
from datetime import date


class ToDoList:
    def __init__(self, title, date):
        self.title = title
        self.date = date
        self.tasks = []

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = date.fromisoformat(value)

    def add(self, task):
        self.tasks.append(task)

    def edit(self, previous, current):
        index = self.tasks.index(previous)
        self.tasks[index] = current

    def delete(self, task):
        self.tasks.remove(task)

    def filter(self, **kwargs):
        if not kwargs:
            return []
        filtered = [
            task for task in self.tasks
            if all(
                getattr(task, key, None) == value for key, value in kwargs.items()
            )
        ]
        return filtered

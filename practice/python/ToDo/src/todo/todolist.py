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

    def delete(self, task):
        self.tasks.remove(task)

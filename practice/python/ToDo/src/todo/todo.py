"""
The ToDo class
"""
from datetime import date

from .enums import Repeat, Priority

class ToDo:
    def __init__(self, task, due, priority=Priority.LOW, repeat=Repeat.NONE, is_complete=False, note=""):
        self.task = task
        self.due = due
        self.priority = priority
        self.repeat = repeat
        self.is_complete = is_complete
        self.note = note

    @property
    def due(self):
        return self._due

    @due.setter
    def due(self, value):
        self._due = date.fromisoformat(value)

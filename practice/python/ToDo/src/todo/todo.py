"""
The ToDo class
"""
from datetime import date
from enum import Enum, auto


class Repeat(Enum):
    NONE = auto()
    DAILY = auto()
    WEEKDAYS = auto()
    WEEKLY = auto()
    MONTHLY = auto()
    QUARTERLY = auto()
    YEARLY = auto()
    CUSTOM = auto()


class ToDo:
    def __init__(self, task, due, repeat=Repeat.NONE, note=""):
        self.task = task
        self.due = due
        self.repeat = repeat
        self.note = note

    @property
    def due(self):
        return self._due

    @due.setter
    def due(self, value):
        self._due = date.fromisoformat(value)

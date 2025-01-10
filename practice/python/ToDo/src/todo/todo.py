"""
The ToDo class
"""
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
        self._task = task
        self._due = due
        self._repeat = repeat
        self._note = note

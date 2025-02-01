"""
Enums
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


class Priority(Enum):
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

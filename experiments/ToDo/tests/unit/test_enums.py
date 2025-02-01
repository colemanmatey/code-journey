"""
Unit tests for the `Repeat` enum.
"""
from todo.enums import Repeat, Priority


def test_repeat_members():
    assert Repeat.NONE.name == 'NONE'
    assert Repeat.DAILY.name == 'DAILY'
    assert Repeat.WEEKDAYS.name == 'WEEKDAYS'
    assert Repeat.WEEKLY.name == 'WEEKLY'
    assert Repeat.MONTHLY.name == 'MONTHLY'
    assert Repeat.QUARTERLY.name == 'QUARTERLY'
    assert Repeat.YEARLY.name == 'YEARLY'
    assert Repeat.CUSTOM.name == 'CUSTOM'


def test_priority_members():
    assert Priority.HIGH.name == 'HIGH'
    assert Priority.MEDIUM.name == 'MEDIUM'
    assert Priority.LOW.name == 'LOW'

"""
Unit tests for the `Repeat` enum.
"""
from todo.todo import Repeat


def test_enum_members():
    assert Repeat.NONE.name == 'NONE'
    assert Repeat.DAILY.name == 'DAILY'
    assert Repeat.WEEKDAYS.name == 'WEEKDAYS'
    assert Repeat.WEEKLY.name == 'WEEKLY'
    assert Repeat.MONTHLY.name == 'MONTHLY'
    assert Repeat.QUARTERLY.name == 'QUARTERLY'
    assert Repeat.YEARLY.name == 'YEARLY'
    assert Repeat.CUSTOM.name == 'CUSTOM'

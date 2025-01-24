"""
Unit tests for the `ToDo` module.
"""
import datetime as dt
import pytest  # type: ignore

from todo.todo import ToDo
from todo.enums import Repeat, Priority


def test_todo_instantiation():
    todo = ToDo(task='Go to work', due='2025-01-08',
                repeat=Repeat.DAILY, note="Additional info")
    assert todo.task == 'Go to work'
    assert todo.due == dt.date(2025, 1, 8)
    assert todo.priority == Priority.LOW
    assert todo.repeat == Repeat.DAILY
    assert todo.is_complete == False
    assert todo.note == 'Additional info'


def test_task_does_not_repeat_by_default():
    todo = ToDo(task='Go to work', due='2025-01-08')
    assert todo.repeat == Repeat.NONE


def test_incorrect_date_format_raises_exception():
    todo = ToDo(task='Visit the park', due='2025-01-08')
    with pytest.raises(ValueError, match="Date did not match this format: YYYY-MM-DD"):
        todo.due = '2025/01/08'

"""
Unit tests for the `ToDo` module.
"""
import datetime
from todo.todo import ToDo, Repeat


def test_todo_instantiation():
    todo = ToDo(task='Go to work', due='2025-01-08', repeat=Repeat.DAILY, note="Additional info")
    assert todo.task == 'Go to work'
    assert todo.due == datetime.date(2025, 1, 8)
    assert todo.repeat == Repeat.DAILY
    assert todo.note == 'Additional info'


def test_task_does_not_repeat_by_default():
    todo = ToDo(task='Go to work', due='2025-01-08')
    assert todo.repeat == Repeat.NONE



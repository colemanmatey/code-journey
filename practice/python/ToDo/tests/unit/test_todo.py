"""
Unit tests for the `ToDo` module.
"""
from todo.todo import ToDo, Repeat

def test_instantiation():
    todo = ToDo(task='Go to work', due='2025-01-08', repeat=Repeat.DAILY, note="Additional info")
    assert todo._task == 'Go to work'
    assert todo._due == '2025-01-08'
    assert todo._repeat == Repeat.DAILY
    assert todo._note == 'Additional info'

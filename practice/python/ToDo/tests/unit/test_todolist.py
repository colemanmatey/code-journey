"""
Unit tests for the `ToDoList` module.
"""
import pytest # type: ignore
from datetime import date
from todo.todolist import ToDoList

@pytest.fixture
def todolist():
    yield ToDoList(title='House chores', date="2925-01-09")

def test_todolist_instantiation(todolist):
    assert todolist.title == 'House chores'

def test_todo_list_date_is_converted_to_date_object(todolist):
    assert isinstance(todolist.date, date) == True

def test_new_todo_list_is_empty(todolist):
    assert len(todolist.tasks) == 0

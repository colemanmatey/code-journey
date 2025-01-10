"""
Unit tests for the `ToDoList` module.
"""
from datetime import date
from todo.todo import ToDoList


def test_todolist_instantiation():
    todolist = ToDoList(title='House chores', date="2925-01-09")
    assert todolist.title == 'House chores'

def test_todo_list_date_is_converted_to_date_object():
    todolist = ToDoList(title='House chores', date="2925-01-09")
    assert isinstance(todolist.date, date) == True

def test_new_todo_list_is_empty():
    todolist = ToDoList(title="Weekend chores", date="2925-01-09")
    assert todolist.tasks == []

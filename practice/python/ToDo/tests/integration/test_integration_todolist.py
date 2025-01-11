"""
Integration tests for the `ToDoList` module.
"""
import pytest # type: ignore
from todo.todo import ToDo, Repeat
from todo.todolist import ToDoList

@pytest.fixture
def data():
    task = ToDo(task='Visit the salon', due='2025-01-08', repeat=Repeat.DAILY, note="")
    todolist = ToDoList(title="Weekend chores", date="2925-01-09")
    todolist.add(task)
    yield task, todolist
    

def test_add_item_to_todo_list(data):
    task, todolist = data
    assert task in todolist.tasks


def test_delete_task_from_todo_list(data):
    task, todolist = data
    todolist.delete(task)
    assert len(todolist.tasks) == 0

def test_edit_task_modifies_task_in_list(data):
    task, todolist = data
    pass
    

"""
Integration tests for the `ToDoList` module.
"""
from todo.todo import ToDo, ToDoList, Repeat


def test_add_item_to_todo_list():
    task = ToDo(task='Visit the salon', due='2025-01-08', repeat=Repeat.DAILY, note="")
    todolist = ToDoList(title="Weekend chores", date="2925-01-09")
    todolist.add(task)
    assert todolist.tasks == [task]


def test_delete_task_from_todo_list():
    task = ToDo(task='Visit the salon', due='2025-01-08', repeat=Repeat.DAILY, note="")
    todolist = ToDoList(title="Weekend chores", date="2925-01-09")
    todolist.tasks.append(task)
    todolist.delete(task)
    assert todolist.tasks == []


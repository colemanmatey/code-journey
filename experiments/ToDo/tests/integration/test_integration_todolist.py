"""
Integration tests for the `ToDoList` module.
"""
import datetime as dt
import pytest  # type: ignore

from todo.todo import ToDo
from todo.todolist import ToDoList
from todo.enums import Repeat, Priority


@pytest.fixture
def data():
    task1 = ToDo(task='Visit the salon', due='2025-01-08',
                 repeat=Repeat.DAILY, note="", is_complete=False)
    task2 = ToDo(task='Buy groceries', due='2025-01-09',
                 repeat=Repeat.DAILY, note="Milk, eggs", is_complete=False)
    task3 = ToDo(task='Finish Python project', due='2025-01-12',
                 repeat=Repeat.WEEKLY, note="Complete the tests", is_complete=True)
    task4 = ToDo(task='Clean the house', due='2025-01-09',
                 repeat=Repeat.MONTHLY, note="", is_complete=False)

    todolist = ToDoList(title="Weekend chores", date="2925-01-09")
    todolist.add(task1)
    todolist.add(task2)
    todolist.add(task3)
    todolist.add(task4)

    yield task1, task2, task3, task4, todolist


def test_add_item_to_todo_list(data):
    task5 = ToDo(task='Learn Geography', due='2025-01-19',
                 repeat=Repeat.DAILY, note="", is_complete=False)
    _, _, _, _, todolist = data
    todolist.add(task5)
    assert task5 in todolist.tasks


def test_delete_task_from_todo_list(data):
    task1, _, _, task4, todolist = data
    todolist.delete(task4)
    assert len(todolist.tasks) == 3
    assert task4 not in todolist.tasks


def test_edit_task_modifies_task_in_list(data):
    task1, _, _, _, todolist = data
    new_task = ToDo(task='Visit the spa', due='2025-01-11',
                    repeat=Repeat.WEEKLY, note="Appointment at 3 PM", is_complete=True)
    todolist.edit(task1, new_task)

    assert task1 not in todolist.tasks
    assert new_task in todolist.tasks

    assert new_task.task == 'Visit the spa'
    assert new_task.due == dt.date.fromisoformat("2025-01-11")
    assert new_task.repeat == Repeat.WEEKLY
    assert new_task.is_complete is True
    assert new_task.note == "Appointment at 3 PM"


def test_filter_returns_empty_list_when_no_condition_is_provided(data):
    task1, task2, task3, task4, todolist = data
    filtered = todolist.filter()
    assert len(filtered) == 0
    assert task1 not in filtered
    assert task2 not in filtered
    assert task3 not in filtered
    assert task4 not in filtered


def test_filter_tasks_by_due_date(data):
    _, task2, _, task4, todolist = data
    filtered = todolist.filter(due=dt.date.fromisoformat('2025-01-09'))
    assert len(filtered) == 2
    assert task2 in filtered
    assert task4 in filtered


def test_filter_tasks_by_completed(data):
    task1, task2, task3, task4, todolist = data
    completed = todolist.filter(is_complete=True)
    assert len(completed) == 1
    assert task1 not in completed
    assert task2 not in completed
    assert task3 in completed
    assert task4 not in completed

    incomplete = todolist.filter(is_complete=False)
    assert len(incomplete) == 3
    assert task1 in incomplete
    assert task2 in incomplete
    assert task3 not in incomplete
    assert task4 in incomplete


def test_filter_tasks_by_repeat(data):
    task1, task2, task3, task4, todolist = data
    daily = todolist.filter(repeat=Repeat.DAILY)
    assert len(daily) == 2
    assert task1 in daily
    assert task2 in daily
    assert task3 not in daily
    assert task4 not in daily

    weekly = todolist.filter(repeat=Repeat.WEEKLY)
    assert len(weekly) == 1
    assert task1 not in weekly
    assert task2 not in weekly
    assert task3 in weekly
    assert task4 not in weekly


def test_filter_tasks_by_priority(data):
    task1, _, _, _, todolist = data
    task1.priority = Priority.HIGH

    high_priority = todolist.filter(priority=Priority.HIGH)
    assert len(high_priority) == 1
    assert task1 in high_priority

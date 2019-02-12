#!/usr/bin/python3
"""
Query a REST API for data then export that data in JSON format
"""
import json
from requests import get
from sys import argv


def export_all_tasks():
    """
    argv = employee ID
    Return: all tasks from all employees lin JSON
    """
    user_info = get("https://jsonplaceholder.typicode.com/users").json()

    todo_data = get("https://jsonplaceholder.typicode.com/todos").json()

    with open("todo_all_employees.json", 'w') as expfile:

        all_tasks_dict = {}

        for user in user_info:
            all_tasks = []
            username = user.get('username')
            user_id = user.get('id')

            for task in todo_data:
                if task.get('userId') == user_id:
                    task_dict = {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": username
                        }
                    all_tasks.append(task_dict)
            all_tasks_dict.update({user_id: all_tasks})

        json.dump(all_tasks_dict, expfile)


if __name__ == "__main__":
    export_all_tasks()

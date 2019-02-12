#!/usr/bin/python3
"""
Query a REST API for data then export that data in JSON format
"""
import json
from requests import get
from sys import argv


def export_tasks(emp_id):
    """
    argv = employee ID
    Return: recorded info about the employee's TODO list progress in JSON
    """
    user_info = get("https://jsonplaceholder.typicode.com/users",
                    params={'id': emp_id}).json()
    todo_data = get("https://jsonplaceholder.typicode.com/todos",
                    params={'userId': emp_id}).json()

    emp_name = user_info[0].get('username')

    with open("{}.json".format(emp_id), 'w') as expfile:
        emp_tasks = []
        for task in todo_data:
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": emp_name
            }
            emp_tasks.append(task_dict)
        emp_data = {emp_id: emp_tasks}
        json.dump(emp_data, expfile)
if __name__ == "__main__":
    if argv[1].isdigit():
        export_tasks(argv[1])

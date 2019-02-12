#!/usr/bin/python3
"""
Query a REST API for data
"""
from sys import argv
from requests import get


def get_todos(emp_id):
    """
    argv = employee ID
    Return: information about the employee's TODO list progress
    """
    user_info = get("https://jsonplaceholder.typicode.com/users",
                    params={'id': emp_id}).json()
    todo_data = get("https://jsonplaceholder.typicode.com/todos",
                    params={'userId': emp_id}).json()
    progress_data = get("https://jsonplaceholder.typicode.com/todos",
                        params={'userId': emp_id, 'completed': 'true'}).json()

    emp_name = user_info[0].get('name')
    emp_tasks = len(todo_data)
    emp_prog = len(progress_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, emp_prog, emp_tasks))

    for task in progress_data:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    if argv[1].isdigit():
        get_todos(argv[1])

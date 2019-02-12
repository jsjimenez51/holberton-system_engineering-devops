#!/usr/bin/python3
"""
Query a REST API for data then export that data in CSV format
"""
import csv
from requests import get
from sys import argv


def export_tasks(emp_id):
    """
    argv = employee ID
    Return: recorded information about the employee's TODO list progress in CSV
    """
    user_info = get("https://jsonplaceholder.typicode.com/users",
                    params={'id': emp_id}).json()
    todo_data = get("https://jsonplaceholder.typicode.com/todos",
                    params={'userId': emp_id}).json()

    emp_name = user_info[0].get('username')

    with open('{}.csv'.format(emp_id), 'w', newline='',
              encoding='utf-8') as csvfile:
        data = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            data.writerow([emp_id,
                          emp_name,
                          task.get('completed'),
                          task.get('title')])


if __name__ == "__main__":
    if argv[1].isdigit():
        export_tasks(argv[1])

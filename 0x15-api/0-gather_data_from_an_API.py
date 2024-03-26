#!/usr/bin/python3
'''python script that returns a ToDo list progress when given an ID'''
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = int(argv[1])  # Convert user ID to integer

    # Fetching todos data
    response = get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()

    # Filter tasks by user ID
    user_tasks = [task for task in data if task['userId'] == user_id]
    total_tasks = len(user_tasks)
    tasks_done = sum(task['completed'] for task in user_tasks)

    # Fetching user info
    response = get(
'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    )
    user_info = response.json()
    employee_name = user_info['name']

    # Printing task completion status
    print(
"Employee {} has done ({}/{}) tasks:".format(employee_name, tasks_done, total_tasks)
        )
    for task in user_tasks:
        if task['completed']:
            print("\t{}".format(task['title']))

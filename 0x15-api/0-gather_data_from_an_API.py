#!/usr/bin/python3
'''python script that returns a ToDo list progress when given an ID'''
import json
import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()
    user_id = int(input("insert your ID number: "))

    user_tasks = [task for task in data if task['userId'] == user_id]

    total_tasks = len(user_tasks)
    tasks_done = sum(task['completed'] for task in user_tasks)

    user_info = requests.get
    ('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    employee_name = user_info['name']

    print("Employee {} has done ({}/{})".format(employee_name, tasks_done,
    total_tasks))

    for task in user_tasks:
        if task['completed']:
            print("\t{}".format(task['title']))

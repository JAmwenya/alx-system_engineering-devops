#!/usr/bin/python3
'''python script that returns a ToDo list progress when given an ID'''
import json
import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()
    user_id = int(input("insert your ID number: "))

# Filter tasks for the given user_id
    user_tasks = [task for task in data if task['userId'] == user_id]

# Count total tasks and completed tasks
    total_tasks = len(user_tasks)
    tasks_done = sum(task['completed'] for task in user_tasks)

# Fetch user info
    user_info = requests.get
    (f'https://jsonplaceholder.typicode.com/users/{user_id}').json()
    employee_name = user_info['name']

# Print progress
    print(f"Employee {employee_name} has done ({tasks_done}/{total_tasks}):")

# Print titles of completed tasks
    for task in user_tasks:
        if task['completed']:
            print(f"\t{task['title']}")

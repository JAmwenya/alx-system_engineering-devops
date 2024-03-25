#!/usr/bin/python3
'''python script that returns a ToDo list progress when given an ID'''
import requests
import json


if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
#print(response.status_code)
#print(response.json())

    data = response.json()

    user_id = int(input("insert your ID number: "))

# Filter tasks for the given user_id
    user_tasks = [task for task in data if task['userId'] == user_id]

# Count total tasks and completed tasks
    total_tasks = len(user_tasks)
    completed_tasks = sum(task['completed'] for task in user_tasks)

# Fetch user info
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}').json()
    employee_name = user_info['name']

# Print progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

# Print titles of completed tasks
    for task in user_tasks:
        if task['completed']:
            print(f"\t{task['title']}")
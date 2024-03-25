#!/usr/bin/python3
#python script that returns a ToDo list progress when given an ID
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
print(response.status_code)
print(response.json())

user_id = int(input("insert your ID number: "))


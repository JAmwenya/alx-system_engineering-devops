#!/usr/bin/python3

"""
Python script that exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
	# Fetching todos data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
	
	#Fetching user info
    row = []
    info_url = get('https://jsonplaceholder.typicode.com/users')
    data2 = info_url.json()

    for i in data2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:

            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                writ.writerow(row)

#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    to_do = get('https://jsonplaceholder.typicode.com/todos/')
    to_do_response = to_do.json()
    users = get('https://jsonplaceholder.typicode.com/users/')
    users_response = users.json()
    completed = 0
    total = 0
    tasks = []

    for i in users_response:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in to_do_response:
        if i.get('userId') == int(argv[1]):
            total += 1
            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))
    for i in tasks:
        print("\t {}".format(i))

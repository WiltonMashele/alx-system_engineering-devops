#!/usr/bin/python3
"""
Returns information about the employee's TODO list progress
and exports data in CSV format.
"""
import csv
import requests
import sys


def fetch_user_data(userid, url):
    user_url = f'{url}users/{userid}'
    response = requests.get(user_url)
    user_info = response.json()
    username = user_info.get('username')
    return username


def fetch_user_tasks(userid, username, url):
    todos_url = f'{url}todos?userId={userid}'
    response = requests.get(todos_url)
    tasks = response.json()
    task_list = []
    for task in tasks:
        task_list.append([userid, username, task.get('completed'),
                            task.get('title')])
    return task_list


def save_tasks_to_csv(filename, task_list):
    with open(filename, mode='w', newline='') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL)
        for task in task_list:
            employee_writer.writerow(task)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <userid>")
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/'
    userid = sys.argv[1]

    username = fetch_user_data(userid, url)
    task_list = fetch_user_tasks(userid, username, url)
    filename = f'{userid}.csv'
    save_tasks_to_csv(filename, task_list)

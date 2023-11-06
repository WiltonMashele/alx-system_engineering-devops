#!/usr/bin/python3
"""
Python script to export data in the JSON format.
Records all tasks from all employees
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users_endpoint = f'{url}users'
    users_response = requests.get(users_endpoint)
    users_data = users_response.json()

    user_tasks = {}
    for user_data in users_data:
        name = user_data.get('username')
        user_id = user_data.get('id')
        todos_endpoint = f'{url}todos?userId={user_id}'
        todos_response = requests.get(todos_endpoint)
        tasks = todos_response.json()
        task_list = []
        for task in tasks:
            task_dict = {
                "username": name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            task_list.append(task_dict)

        user_tasks[str(user_id)] = task_list

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as file:
        json.dump(user_tasks, file)

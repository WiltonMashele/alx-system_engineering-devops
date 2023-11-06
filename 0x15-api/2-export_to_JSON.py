#!/usr/bin/python3
"""script to export data in the JSON format"""

import json
import requests
import sys


def export_tasks_to_json(user_id, tasks):
    user_tasks = {str(user_id): tasks}
    filename = f'{user_id}.json'
    with open(filename, mode='w') as file:
        json.dump(user_tasks, file)


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user_endpoint = f'{url}users/{user_id}'
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    username = user_data.get('username')
    print(username)

    todos_endpoint = f'{url}todos?userId={user_id}'
    todos_response = requests.get(todos_endpoint)
    tasks = todos_response.json()
    print(tasks)

    task_list = []
    for task in tasks:
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
        task_list.append(task_dict)

    export_tasks_to_json(user_id, task_list)

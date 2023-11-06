#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user_endpoint = '{}users/{}'.format(url, user_id)
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    username = user_data.get('username')
    print(username)

    todos_endpoint = '{}todos?userId={}'.format(url, user_id)
    todos_response = requests.get(todos_endpoint)
    tasks = todos_response.json()
    print(tasks)
    
    task_list = []
    for task in tasks:
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": username}
        task_list.append(task_dict)

    user_tasks = {str(user_id): task_list}
    filename = '{}.json'.format(user_id)
    with open(filename, mode='w') as file:
        json.dump(user_tasks, file)

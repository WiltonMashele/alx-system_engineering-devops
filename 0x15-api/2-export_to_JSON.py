#!/usr/bin/python3
"""script to export data in the JSON format"""


import json
import requests
import sys

def get_user_info(userid):
    url = 'https://jsonplaceholder.typicode.com/'

    user_url = f'{url}users/{userid}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')
    print(username)

    todos_url = f'{url}todos?userId={userid}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    task_list = []


    for task in todos_data:
        task_info = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        task_list.append(task_info)

    user_tasks = {str(userid): task_list}
    filename = f'{userid}.json'

    with open(filename, mode='w') as file:
        json.dump(user_tasks, file)

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python script.py <userid>")
        sys.exit(1)

    userid = sys.argv[1]
    get_user_info(userid)

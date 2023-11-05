#!/usr/bin/python3
""" script to export data in the JSON format."""
import requests
import sys
import json

if __name__ == "__main":
    url = "https://jsonplaceholder.typicode.com/"
    user_ids = range(1, 11)
    all_data = {}

    for user_id in user_ids:
        user = requests.get(url + "users/{}".format(user_id)).json()
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        user_tasks = [{"username": user.get("username"), "task": task.get("title"), "completed": task.get("completed")} for task in todos]

        all_data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file, indent=2)

    print("Data exported to todo_all_employees.json")

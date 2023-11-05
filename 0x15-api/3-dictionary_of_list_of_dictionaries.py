#!/usr/bin/python3
""" script to export data in the JSON format."""
import requests
import sys
import json

def get_employee_tasks(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{user_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    employee_tasks = []

    for todo in todos:
        employee_tasks.append({
            "username": user['username'],
            "task": todo["title"],
            "completed": todo["completed"]
        })

    return user_id, employee_tasks

if __name__ == "__main":
    if len(sys.argv) < 2:
        print("Usage: python script.py USER_ID")
        sys.exit(1)

    user_id = sys.argv[1]

    all_employees_tasks = {}

    user_ids = [1, 2, 3, 4, 5]

    for user_id in user_ids:
        user_id, tasks = get_employee_tasks(user_id)
        all_employees_tasks[user_id] = tasks

    # Export data to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

    print("Data exported to todo_all_employees.json")

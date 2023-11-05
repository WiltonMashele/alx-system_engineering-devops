#!/usr/bin/python3
"""Returns information about the employee's TODO list progress."""

import sys
import requests
import urllib.request

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        with urllib.request.urlopen(user_url) as response:
            user_data = response.read().decode('utf-8')
        with urllib.request.urlopen(todo_url) as response:
            todo_data = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
        sys.exit(1)

    user = json.loads(user_data)
    todos = json.loads(todo_data)

    completed_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)

    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    main()

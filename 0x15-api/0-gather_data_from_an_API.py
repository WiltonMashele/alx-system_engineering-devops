#!/usr/bin/python3
"""Returns information about the employee's TODO list progress."""

import json
import sys
import urllib.request as fetcher

def fetch_user_data(user_id):
    endpoint = 'https://jsonplaceholder.typicode.com'
    name_url = f'/users/{user_id}'
    todos_url = f'{name_url}/todos'

    try:
        with fetcher.urlopen(endpoint + name_url) as res:
            user_data = res.read()
        with fetcher.urlopen(endpoint + todos_url) as res:
            todos_data = res.read()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    user = json.loads(user_data)
    todos = json.loads(todos_data)

    return user, todos

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    user, todos = fetch_user_data(user_id)

    completed_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)

    print("Employee {} is done with tasks ({}/{}):".format(
        user["name"], len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task["title"]))

if __name__ == "__main__":
    main()

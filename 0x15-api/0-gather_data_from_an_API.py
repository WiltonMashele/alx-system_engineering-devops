#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user = requests.get(url).json()

    url = f"https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(url, params={"userId": employee_id}).json()

    completed_tasks = [task["title"] for task in todos if task["completed"]]

    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))

    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    main()

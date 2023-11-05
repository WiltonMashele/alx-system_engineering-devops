#!/usr/bin/python3
"""Returns information about the employee's TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f"{url}users/{user_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    completed = [t["title"] for t in todos if t["completed"]]
    print(f"Employee {user['name']} is done with tasks({len(completed)}/{len(todos)}):")
    [print(f"\t {c}") for c in completed]

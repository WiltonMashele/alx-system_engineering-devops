#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""
import requests
import sys
import csv

if __name__ == "__main":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f"{url}users/{user_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    completed_tasks = [t for t in todos if t["completed"]]
    task_count = len(todos)

    # Create a CSV file for the user
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in completed_tasks:
            csv_writer.writerow([user['id'], user['name'], "Completed", task['title']])

    print(f"Employee {user['name']} is done with tasks ({len(completed_tasks)}/{task_count}).")
    print(f"Data exported to {csv_filename}")

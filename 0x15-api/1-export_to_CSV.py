#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to a CSV file."""
import requests
import csv
import sys

if __name__ == "__main":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f"{url}users/{user_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    csv_file_name = f"{user_id}.csv"

    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for todo in todos:
            task_completed_status = "Completed" if todo["completed"] else "Not Completed"
            task_title = todo["title"]
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user["name"],
                "TASK_COMPLETED_STATUS": task_completed_status,
                "TASK_TITLE": task_title
            })

    print(f"Data exported to {csv_file_name}")

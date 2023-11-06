#!/usr/bin/python3
"""Returns information about the employee's TODO list progress and exports data in CSV format."""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f"{url}users/{user_id}").json()
    todos = requests.get(
        f"{url}todos", params={"userId": user_id}
    ).json()

    completed = [t for t in todos if t["completed"]]
    employee_name = user['name']


    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for task in completed:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": "completed",
                "TASK_TITLE": task["title"]
            })

    print(f"Data has been exported to {csv_filename}")

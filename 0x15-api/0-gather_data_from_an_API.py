#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

def truncate_name(name, max_length=18):
    if len(name) > max_length:
        return name[:max_length] + "..."
    return name

if __name__ == "__main__":
    try:
        userId = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Fetch user details
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    if user_response.status_code != 200:
        print(f"User with ID {userId} not found.")
        sys.exit(1)

    user = user_response.json()
    name = user.get('name')
    truncated_name = truncate_name(name)

    # Fetch todos for the user
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}/todos")
    if todos_response.status_code != 200:
        print(f"Could not retrieve todos for user with ID {userId}.")
        sys.exit(1)

    todos = todos_response.json()
    totalTasks = len(todos)
    completedTasks = [task for task in todos if task.get('completed')]

    print(f'Employee {truncated_name} is done with tasks({len(completedTasks)}/{totalTasks}):')
    for task in completedTasks:
        print(f"\t {task.get('title')}")

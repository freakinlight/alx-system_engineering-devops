#!/usr/bin/python3
"""
Module to fetch and display all employees' TODO list progress using a REST API.
Exports the data in JSON format.
"""

import json
import requests


def get_all_employees_todo_progress():
    """
    Fetch and display the TODO list progress for all employees.
    Export the data in JSON format.
    """
    try:
        # Fetch all users information
        users_url = 'https://jsonplaceholder.typicode.com/users'
        users_response = requests.get(users_url)
        users_data = users_response.json()

        if not users_data:
            print("No users found")
            return

        all_tasks = {}

        # Pre-initialize dictionary for all users to handle users with no tasks
        for user in users_data:
            user_id = str(user.get('id'))
            all_tasks[user_id] = []  # Initialize each user with an empty list of tasks

        # Populate tasks for each user
        todos_url = 'https://jsonplaceholder.typicode.com/todos'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        for task in todos_data:
            user_id = str(task.get('userId'))
            task_info = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": next(user.get('username') for user in users_data if user.get('id') == task.get('userId'))
            }
            all_tasks[user_id].append(task_info)

        # Write data to JSON file
        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as json_file:
            json.dump(all_tasks, json_file)

        print(f"Data exported to {json_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_all_employees_todo_progress()

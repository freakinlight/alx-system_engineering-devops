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

        for user in users_data:
            user_id = str(user.get('id'))
            username = user.get('username')

            # Fetch user's TODO list
            todos_url = (
                f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
            )
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            tasks = []
            for task in todos_data:
                tasks.append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                })

            all_tasks[user_id] = tasks

        # Write data to JSON file
        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(all_tasks, json_file)

        print(f"Data exported to {json_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_all_employees_todo_progress()

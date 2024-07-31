#!/usr/bin/python3
"""
Module to fetch and display an employee's TODO list progress using a REST API.
Exports the data in JSON format.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.
    Export the data in JSON format.
    """
    try:
        # Fetch employee information
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user_data = user_response.json()

        if not user_data:
            print(f"No user found for employee ID {employee_id}")
            return

        employee_username = user_data.get('username')

        # Fetch employee's TODO list
        todos_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        if not todos_data:
            print(f"No TODOs found for employee ID {employee_id}")
            return

        # Prepare data for JSON file
        tasks = []
        for task in todos_data:
            tasks.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_username
            })

        # Write data to JSON file
        json_filename = f"{employee_id}.json"
        with open(json_filename, mode='w') as json_file:
            json.dump({employee_id: tasks}, json_file)

        print(f"Data exported to {json_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

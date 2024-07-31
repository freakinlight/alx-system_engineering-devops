#!/usr/bin/python3
"""
Module to fetch and display an employee's TODO list progress using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.
    """
    try:
        # Fetch employee information
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user_data = user_response.json()

        if not user_data:
            print(f"No user found for employee ID {employee_id}")
            return

        employee_name = user_data.get('name')

        # Fetch employee's TODO list
        todos_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        if not todos_data:
            print(f"No TODOs found for employee ID {employee_id}")
            return

        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get('completed')]
        number_of_done_tasks = len(done_tasks)

        # Display TODO list progress
        print(
            f"Employee {employee_name} is done with tasks("
            f"{number_of_done_tasks}/{total_tasks}):"
        )
        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

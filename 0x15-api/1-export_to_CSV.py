#!/usr/bin/python3
"""
Module to fetch and display an employee's TODO list progress using a REST API.
Exports the data in CSV format.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.
    Export the data in CSV format.
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

        # Write data to CSV file
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow([
                    employee_id,
                    employee_username,
                    task.get('completed'),
                    task.get('title')
                ])

        print(f"Data exported to {csv_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

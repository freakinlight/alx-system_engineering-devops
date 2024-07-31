#!/usr/bin/python3
import requests
import sys


def fetch_data(employee_id):
    # URL to the API endpoint
    api_url = 'https://jsonplaceholder.typicode.com'
    # Fetching user data
    user_url = f'{api_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user = user_response.json()
    # Fetching todos data
    todos_url = f'{api_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    # Calculating TODO list progress
    total_tasks = len(todos)
    completed_tasks = len([task for task in todos if task['completed']])
    # Printing the progress
    print(
        f"Employee {user['name']} is done with tasks("
        f"{completed_tasks}/{total_tasks}):"
    )
    for task in todos:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee id>")
    else:
        fetch_data(int(sys.argv[1]))

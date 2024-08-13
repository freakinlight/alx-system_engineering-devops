#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    # Define the URL
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set up headers to avoid Too Many Requests error
    headers = {'User-Agent': 'my-app/0.0.1'}

    # Make the GET request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0

#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and print the titles
of the first 10 hot posts for a given subreddit.
"""


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles of the first 10 hot posts
        or 'None' if the subreddit is invalid.
    """
    import requests

    # Define the URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set up headers to avoid Too Many Requests error
    headers = {'User-Agent': 'alx-project:v1.0 (by /u/your_reddit_username)'}

    # Make the GET request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title'))
    else:
        print(None)

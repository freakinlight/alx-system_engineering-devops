#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set up headers to avoid Too Many Requests error
    headers = {'User-Agent': 'alx-project:v1.0 (by /u/your_reddit_username)'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    else:
        return 0

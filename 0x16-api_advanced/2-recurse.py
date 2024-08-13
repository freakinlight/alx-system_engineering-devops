#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API and return
a list of all hot article titles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list of titles of all hot
    articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list of titles collected so far.
        after (str): The 'after' parameter for pagination (used in recursion).

    Returns:
        list: A list of titles of all hot articles,
        or None if the subreddit is invalid.
    """
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set up headers to avoid Too Many Requests error
    headers = {'User-Agent': 'alx-project:v1.0 (by /u/your_reddit_username)'}

    # Define parameters for the request, including pagination
    params = {'limit': 100, 'after': after}

    # Make the GET request to the Reddit API
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    # Check if the request was successful
    if response.status_code != 200:
        return None

    # Parse the JSON response and extract the relevant data
    data = response.json().get('data', {})
    children = data.get('children', [])

    # Append each title to the hot_list
    for child in children:
        hot_list.append(child.get('data', {}).get('title'))

    # Get the 'after' value for pagination
    after = data.get('after')

    # If there is more data to retrieve, call the function recursively
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        # Base case: return the accumulated list of titles
        return hot_list

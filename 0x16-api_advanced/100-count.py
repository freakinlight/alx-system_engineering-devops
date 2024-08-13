#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API, parse
the titles of all hot articles, and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively query the Reddit API, parse the titles of all hot articles,
    and count the occurrences of specific keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): The 'after' parameter for pagination (used in recursion).
        word_count (dict): A dictionary to store counts of keywords.

    Returns:
        None: Prints the sorted count of keywords or prints nothing if the
              subreddit is invalid or no keywords are found.
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

    # Initialize word_count dictionary during the first call
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    # Count occurrences of each keyword in the titles
    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            word = word.lower()
            word_count[word] += title.split().count(word)

    # Get the 'after' value for pagination
    after = data.get('after')

    # If there is more data to retrieve, call the function recursively
    if after:
        return count_words(subreddit, word_list, after, word_count)

    # Once all pages are processed, sort and print the results
    if word_count:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")

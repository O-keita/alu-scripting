#!/usr/bin/python3

"""
reddit_api_client.py
A simple module for interacting with the Reddit API.

This module provides functions to query the Reddit API and retrieve information about subreddits.

Usage:
1. number_of_subscribers(subreddit): Returns the number of subscribers for a given subreddit.

Note: No authentication is necessary for most features of the Reddit API. Ensure a custom User-Agent is set.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for the given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers, or 0 if the subreddit is not valid or there's an issue with the request.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                return data.get('subscribers', 0)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

    return 0

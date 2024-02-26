#!/usr/bin/python3
"""Getting Started with Reddit

This script retrieves the number of subscribers for a given subreddit using the Reddit API.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """Retrieve the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if an error occurs.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {"User-Agent": "Just a sample school"}

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data.get('data').get('subscribers', 0)
        print(subs)
        return subs

    elif response.status_code == 404:
        print(0)
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0

if __name__ == "__main__":
    """Main entry point."""
    try:
        subreddit_name = sys.argv[1]
        result = number_of_subscribers(subreddit_name)
    except IndexError:
        print("Usage: python script_name.py subreddit_name")

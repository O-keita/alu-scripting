#!/usr/bin/python3
"""
Script that fetches 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts from a subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    None
    """
    headers = {'User-Agent': 'just checking'}
    subreddit_url = f"https://reddit.com/r/{subreddit}/hot.json"
    response = requests.get(subreddit_url, headers=headers, params={'limit': 10})

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])

        if data:
            for single_data in data:
                title = single_data.get('data', {}).get('title', None)

                if title:
                    print(title)
                else:
                    print(None)
        else:
            print(None)
    else:
        print(None)

# Example usage:
# top_ten('python')

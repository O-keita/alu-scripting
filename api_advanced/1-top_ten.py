#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts from a subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    None
    """
    headers = {'User-Agent': 'My User Agent 1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10}  # Limiting to 10 posts

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            for post in data:
                title = post.get('data', {}).get('title')
                print(title)
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

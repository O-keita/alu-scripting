#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the top 10 hot posts from a subreddit."""

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        try:
            json_data = response.json()
            for i in range(10):
                print(
                    json_data.get('data')
                    .get('children')[i]
                    .get('data')
                    .get('title')
                )
        except (KeyError, IndexError):
            print("Error parsing JSON data. Check the subreddit and try again.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Example usage
subreddit_name = "python"
top_ten(subreddit_name)

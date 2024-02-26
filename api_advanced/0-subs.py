#!/usr/bin/python3
"""Getting Started with Reddit"""

import requests
import sys


def number_of_subscribers(subreddit):
    """This is the main function"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {"User-Agent": "Just a sample school"}

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()
        subs = data.get('data').get('subscribers')
        print(subs)
        return subs

    elif response.status_code == 404:
        return None
    else:
        return "Error"


if __name__ == "__main__":
    subreddit_name = sys.argv[1]
    result = number_of_subscribers(subreddit_name)

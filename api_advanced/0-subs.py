#!/usr/bin/python3
"""Api is getting over my head"""

import requests


def number_of_subscribers(subreddit):
    """Function getting the API"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {
        "User-Agent":"getting number of subs"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code ==200:
        data = response.json()

        subs = data.get('data').get('subscribers')

        return subs
    else:
        return 0
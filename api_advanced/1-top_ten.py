#!/usr/bin/python3
"""Documented the main module"""

import requests


def top_ten(subreddit):
    """documented the function """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {"User-Agent":"Just practicing"}

    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:

            datas = response.json().get('data').get('children')

            if datas:

                for data in datas:

                    title = data.get('data').get('title')

                    print(title)

                return title
                
            else:
                return 0
            
        else:
            return 0
        
    except requests.RequestException as e:
        print(e)
    
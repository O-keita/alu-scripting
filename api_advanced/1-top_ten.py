#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""

    headers = {'User-Agent': 'just checking'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url,
                            headers=headers, params={'limit': 10})

    if response.status_code == 200:

        data = response.json().get('data', {}).get('children', [])

        if data:
                    
                for single_data in data:

                    title = single_data.get('data', {}).get('title', None)

                    if title:
                        

                        print(title)
                    else:
                         print(None)



                return title
        else:
             print(None)
             return None

    else:
        return_value = None
        print(return_value)
        return return_value

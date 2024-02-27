import requests

def get_subreddit_subscribers(subreddit):
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

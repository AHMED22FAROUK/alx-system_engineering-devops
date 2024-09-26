#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns.
    the number of subscribers for a given subreddit.
    :param subreddit: The name of the subreddit (str)
    :return: The number of subscribers (int), or 0 if the subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:myredditbot:v1.0.0 (by /u/wassola)"
        }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except requests.RequestException:
            return 0

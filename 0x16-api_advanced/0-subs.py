#!/usr/bin/python3

"""query subscribers function on a given Reddit subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code in [301, 302, 404]:
            return 0
        results = response.json().get("data")
        if results is None:
            return 0
        return results.get("subscribers", 0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

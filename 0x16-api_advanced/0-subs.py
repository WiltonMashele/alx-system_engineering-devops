#!/usr/bin/python3
"""
Module to interact with Reddit API and retrieve subreddit information.
"""
import requests


def get_subreddit_subscribers(subreddit):
    """
    Return the total number of subscribers for a specified subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, 
                allow_redirects=False)
        response.raise_for_status()
        data = response.json()["data"]
        subscribers = data["subscribers"]
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

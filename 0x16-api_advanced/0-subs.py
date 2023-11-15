#!/usr/bin/python3
"""
Module to interact with Reddit API and retrieve subreddit information.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a specified subreddit.
    If not a valid subreddit, return 0.
    """
    headers = {"User-Agent": "0x16.API_advanced-WiltonMashele"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            subscribers = response.json().get("data", {}).get("subscribers", 0)
            return subscribers
        elif response.status_code == 404:
            return 0
        else:
            print(f"Request failed with status code {response.status_code}")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

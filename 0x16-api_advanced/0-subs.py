#!/usr/bin/python3
"""
Sends a query to an api to retrieve data
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns the number of subscribers for a given sub
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'subscriber info'}

    try:
        reddit_data = requests.get(url, headers=headers, allow_redirects=False)
        get_subs = reddit_data.json()['data']['subscribers']
        return (get_subs)

    except BaseException:
        return 0


if __name__ == '__main__':
    number_of_subscribers(subreddit)

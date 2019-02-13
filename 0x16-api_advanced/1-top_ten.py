#!/usr/bin/python3
"""
Sends a query to an api to retrieve data
"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and returns titles for top 10 hot posts for a given sub
    """
    url = 'https://api.reddit.com/r/{}/hot?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Hot Post Info'}

    try:
        reddit_data = requests.get(url, headers=headers, allow_redirects=False)
        get_top = reddit_data.json()['data']['children']
        for title in get_top:
            print(title['data']['title'])

    except BaseException:
        print(None)


if __name__ == '__main__':
    number_of_subscribers(top_ten)

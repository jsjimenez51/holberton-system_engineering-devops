#!/usr/bin/python3
"""
Sends a query to an api to retrieve data
"""
import requests


def recurse(subreddit, after='', hot_list=[]):
    """
    Queries Reddit API and returns titles for hot posts for a given sub
    """
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'User-Agent': 'Hot Post Recursive Grab Info'}
    paginate = {'after': after}
    try:
        reddit_data = requests.get(url, headers=headers, params=paginate,
                                   allow_redirects=False).json()

        all_articles = reddit_data['data']['children']

        for article in all_articles:
            hot_list.append(article['data']['title'])

        next_pg = reddit_data['data']['after']

        if next_pg is None:
            return hot_list

        return recurse(subreddit, next_pg, hot_list)

    except BaseException:
        return None

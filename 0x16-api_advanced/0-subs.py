#!/usr/bin/python3
"""
Returns number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
	"""
	a function that queries the Reddit API and returns the number of subscribers for a given subreddit
	"""


    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Google Chrome Version 123.0.6312.105/106'}
    url = 'https://www.reddit.com/r/dev/api/about.json'
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0

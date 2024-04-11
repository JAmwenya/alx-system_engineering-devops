#!/usr/bin/python3
"""
Returns number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
	"""
	a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit
	"""

    url = f"https://www.reddit.com/r/dev/api/about.json"
    headers = {'User-Agent': 'Google Chrome Version 123.0.6312.105/106'}  
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

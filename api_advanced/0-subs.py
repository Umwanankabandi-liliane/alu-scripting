#!/usr/bin/python3
"""0-subs.py"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            data = response.json().get("data", {})
            subscribers = data.get("subscribers") if data else None
            
            if subscribers is not None:
                return subscribers
            else:
                print(f"No subscribers data found for subreddit: {subreddit}")
                return 0
        else:
            print(f"Error fetching subreddit data: Status Code {response.status_code}")
            return 0
    
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return 0

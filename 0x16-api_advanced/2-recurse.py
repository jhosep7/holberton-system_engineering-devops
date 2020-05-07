#!/usr/bin/python3
"""Return titles """
import requests


def recurse(subreddit, hot_list=[]):
    """Titles Recursive """
    Web = "https://api.reddit.com/r/{}?sort=hot"
    H = {'User-Agent': 'CustomClient/1.0'}
    after = "{}&after={}"
    if type(subreddit) is not list:
        web = Web.format(subreddit)
        subreddit = [subreddit, ""]
    else:
        web = Web.format(subreddit[0])
        web = after.format(web, subreddit[1])
    Req = requests.get(web, headers=H, allow_redirects=False)
    if Req.status_code != 200:
        return (None)
    Req = Req.json()
    if 'data' not in Req:
        return (None)
    else:
        Info = Req.get("data")
        if not Info.get("children"):
            return (hot_list)
        for i in Info.get("children"):
            hot_list += [i.get("data").get("title")]
        if not Info.get("after"):
            return (hot_list)
        subreddit[1] = Info.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return (hot_list)

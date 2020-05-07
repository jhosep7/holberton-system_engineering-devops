#!/usr/bin/python3
""" Get Subscribers reddit """
import requests


def number_of_subscribers(subreddit):
    """ Get subscribers"""
    Web = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    H = {'User-Agent': 'CustomClient/1.0'}
    Req = requests.get(Web, headers=H)
    if Req.status_code != 200:
        return (0)
    Subscribers = Req.json().get('data', {}).get('subscribers', 0)
    return (Subscribers)

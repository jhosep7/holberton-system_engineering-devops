#!/usr/bin/python3
""" top 10"""
import requests


def top_ten(subreddit):
    """ Top 10"""
    Web = 'http://reddit.com/r/{}/hot.json'.format(subreddit)
    H = {'User-Agent': 'CustomClient/1.0'}
    Req = requests.get(Web, headers=H)
    Info = Req.json().get('data', {}).get('children', {})
    if 'data' not in Req.json() or Req.status_code != 200:
        return (print(None))
    [print(i.get('data', {}).get('title')) for i in Info[0:10]]

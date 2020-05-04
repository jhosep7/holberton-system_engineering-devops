#!/usr/bin/python3
"""xport data in the JSON format"""
from sys import argv
import requests
import json


if __name__ == "__main__":
    """export JSON"""
    Id = argv[1]
    N = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(Id)).json()
    ReqT = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(Id)).json()
    Acts = []
    for i in ReqT:
        Act = {}
        Act['task'] = i.get('title')
        Act['completed'] = i.get('completed')
        Act['username'] = N.get('username')
        Acts.append(Act)
    FileInfo = {}
    FileInfo[Id] = Acts
    with open("{}.json".format(Id), 'w') as JSONfile:
        json.dump(FileInfo, JSONfile)

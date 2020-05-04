#!/usr/bin/python3
"""xport data in the JSON format"""
import requests
import json


if __name__ == "__main__":
    """export JSON"""
    N = requests.get("https://jsonplaceholder.typicode.com/users").json()
    ReqT = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    MyDict = {}
    for i in N:
        Id = i.get("id")
        Name = i.get('username')
        for j in ReqT:
            if (j.get('userId') == int(Id)):
                dict = {}
                dict['task'] = i.get('title')
                dict['completed'] = i.get('completed')
                dict['username'] = Name
        MyDict[Id] = ReqT
    with open("todo_all_employees.json", 'w') as JSONfile:
        json.dump(MyDict, JSONfile)

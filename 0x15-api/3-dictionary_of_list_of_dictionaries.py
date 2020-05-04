#!/usr/bin/python3
"""xport data in the JSON format"""
import json
import requests


if __name__ == "__main__":
    """export JSON"""
    N = requests.get("https://jsonplaceholder.typicode.com/users").json()
    ReqT = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    MyDict = {}
    Name = {}
    for i in N:
        Id = i.get("id")
        MyDict[Id] = []
        Name[Id] = i.get('username')
    for j in ReqT:
        Act = {}
        Id = j.get('userId')
        Act['task'] = j.get('title')
        Act['completed'] = j.get('completed')
        Act['username'] = Name.get(Id)
        MyDict.get(Id).append(Act)
    with open("todo_all_employees.json", 'w') as JSONfile:
        json.dump(MyDict, JSONfile)

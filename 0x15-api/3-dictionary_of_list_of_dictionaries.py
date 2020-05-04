#!/usr/bin/python3
"""xport data in the JSON format"""
import json
import requests


if __name__ == "__main__":
    """export JSON"""
    N = requests.get("https://jsonplaceholder.typicode.com/users").json()
    ReqT = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    MyDict = {}
    for i in N:
        Name = [j for j in ReqT if j.get('userId') == i.get('id')]
        Name = [{'username': i.get('username'), 'task': j.get('title'),
                 'completed': j.get('completed')} for j in Name]
        MyDict[str(i.get('id'))] = Name
    with open("todo_all_employees.json", 'w') as JSONfile:
        json.dump(MyDict, JSONfile)

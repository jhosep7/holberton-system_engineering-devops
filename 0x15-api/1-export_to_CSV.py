#!/usr/bin/python3
"""xport data in the CSV format"""
import csv
from csv import writer, QUOTE_ALL
import requests
from sys import argv


if __name__ == "__main__":
    """export CSV"""
    Id = argv[1]
    N = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(Id)).json()
    ReqT = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(Id)).json()
    with open("{}.csv".format(Id), 'w') as CVSfile:
        Writer = writer(CVSfile, delimiter=',', quoting=QUOTE_ALL)
        for i in ReqT:
            Writer.writerow([Id, N.get('username'),
                             i.get('completed'), i.get('title')])

#!/usr/bin/python3
"""sing this REST API, for a given employeeID. return info"""
from sys import argv
import requests


if __name__ == "__main__":
    """Get TODO"""
    Id = int(argv[1])
    N = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(Id)).json()
    ReqT = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(Id)).json()
    Task = [i.get('title') for i in ReqT if i.get('completed') is True]
    VarN = N.get('name')
    print("Employee {} is done with tasks({}/{}):".
          format(VarN, len(Task), len(ReqT)))
    for i in ReqT:
        print("\t {}".format(i))

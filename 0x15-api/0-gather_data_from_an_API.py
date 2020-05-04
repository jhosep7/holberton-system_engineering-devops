#!/usr/bin/python3
"""sing this REST API, for a given employeeID. return info"""
from sys import argv
import requests


if __name__ == "__main__":
    """Get TODO"""
    Id = argv[1]
    N = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(Id)).json()
    ReqT = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(Id)).json()
    VarN = N.get('name')
    ReqForm = [i for i in ReqT if i.get('userId') == N.get('id')]
    DoneT = [i for i in ReqForm if i.get('completed')]
    print("Employee {} is done with tasks({}/{}):".
          format(VarN, len(DoneT), len(ReqForm)))
    [print('\t', i.get('title')) for i in DoneT]

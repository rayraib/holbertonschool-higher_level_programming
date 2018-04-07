#!/usr/bin/python3
'''
     Python script that takes your Github credentials (username and password)
     and uses the Github API to display your id
'''
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    user = sys.argv[1]
    passs = sys.argv[2]

    url = 'https://api.github.com/user'

    r = requests.get('https://api.github.com/user', auth=(user, passs))
    json_obj = r.json()
    try:
        print(json_obj['id'])
    except KeyError:
        print('None')

#!/usr/bin/python3
'''
    Python script that takes in a URL,
    sends a request to the URL and displays the body of the response.
'''
import requests
import sys


if __name__ == "__name__":

    url = sys.argv[1]

    res = reqeusts.get(url)
    if (res.status_code) >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)

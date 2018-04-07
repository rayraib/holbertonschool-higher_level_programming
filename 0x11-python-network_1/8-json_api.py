#!/usr/bin/python3
'''
    Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    
    try:
        q = sys.argv[1]
    else:
        q =""

    res = requests.get(url)
    try:
        json_res = res.json()
        print(json_res)
    except:
        print("not valid")


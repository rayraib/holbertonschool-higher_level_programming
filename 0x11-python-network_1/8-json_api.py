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
        payload = {'q': sys.argv[1]}
    except:
        payload = {'q': ""}

    res = requests.post(url, data=payload)
    try:
        json_res = res.json()
        print("[{}] {}".format(json_res['id'], json_res['name']))
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")
    

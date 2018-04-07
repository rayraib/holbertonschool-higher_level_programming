#!/usr/bin/python3
'''
    Python script that takes in a string and sends a search request
    to the Star Wars API
'''
import requests
import sys


if __name__ == "__main__":

    key_word = sys.argv[1]
    payload = {"search": key_word}
    url = 'https://swapi.co/api/people/?search={}'.format(key_word)

    res = requests.get(url)
    res_dict = res.json()
    print("Number of results: {}".format(res_dict['count']))
    for result in res_dict['results']:
        print(result['name'])

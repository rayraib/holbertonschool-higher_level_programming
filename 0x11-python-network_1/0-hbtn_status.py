#!/usr/bin/python3
'''
    Script to fetch a URL
'''
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print("Body response:")
    print("\t - type: {}".format(type(html)))
    print("\t - content: {}".format(html))
    print("\t - utf8 ontent: {}".format(html.decode()))

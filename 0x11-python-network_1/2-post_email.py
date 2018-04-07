#!/usr/bin/python3
'''
    Python script that takes in a URL and an email,
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}

    # encoding the values to url
    data = urllib.parse.urlencode(values)

    # encoding data to bytes 
    data = data.encode('ascii')

    # req is a urllib.request.Request object
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print (content)

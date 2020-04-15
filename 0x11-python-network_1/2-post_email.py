#!/usr/bin/python3
""" Script that sends a post request """
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        resp = response.read()
        html = resp.decode('UTF-8')
        print(html)

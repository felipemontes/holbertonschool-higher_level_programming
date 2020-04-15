#!/usr/bin/python3
""" Script that handles error codes """
from urllib import request, error
import sys

if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except urllib.error.HTTPError as e:
            print('Error code: {}'.format(e.code))

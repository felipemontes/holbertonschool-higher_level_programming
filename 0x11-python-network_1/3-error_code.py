#!/usr/bin/python3
""" Script that handles error codes """
from urllib import request, error
import sys

if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
        except error.HTTPError as err:
            print('Error code: {}'.format(err.code))

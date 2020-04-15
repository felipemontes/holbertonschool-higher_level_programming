#!/usr/bin/python3
""" searches for a var in the header """
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    x = r.headers['X-Request-Id']
    print(x)

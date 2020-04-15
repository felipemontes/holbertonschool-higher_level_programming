#!/usr/bin/python3
""" python script to get github id """
import requests
import sys

if __name__ == '__main__':

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))

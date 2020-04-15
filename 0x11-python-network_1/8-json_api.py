#!/usr/bin/python3
""" script that sends a post request and returns a json """
import requests
import sys

if __name__ == '__main__':
    value = ''

    if len(sys.argv) == 1:
        value = ''
    else:
        value = sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': value})

    try:
        response = r.json()
        if len(response) == 2:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')

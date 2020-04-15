#!/usr/bin/python3
""" get last commits of a github rep """
import requests
import sys


if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.
                     format(sys.argv[2], sys.argv[1]))
    res = r.json()

    for i in res[:10]:
        sha = i.get('sha')
        author = i.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))

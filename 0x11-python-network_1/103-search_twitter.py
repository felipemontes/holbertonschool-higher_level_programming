#!/usr/bin/python3
""" Twitter API interaction"""
import requests
import sys
import base64

if __name__ == '__main__':

    host = "https://api.twitter.com/oauth2/token"
    cont = "{}:{}".format(sys.argv[1], sys.argv[2])
    cenco = base64.b64encode(cont.encode('utf-8'))

    head = {
        "Authorization": "Basic {}".format(cenco.decode('utf-8')),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    bodyreq = {
        "grant_type": "client_credentials"
    }

    r = requests.post(host, headers=head, data=bodyreq)

    auth = {
        "Authorization": "Bearer {}".format(r.json().get("access_token"))
    }

    resource = "https://api.twitter.com/1.1/search/tweets.json"

    search = {
        "q": sys.argv[3],
        "result_type": "recent",
        "count": 5
    }

    req_search = requests.get(resource, headers=auth, params=search)

    tweet = req_search.json().get("statuses")

    for i in tweets:
        print("[{}] {} by {}").format(i.get("id"), i.get("texts"),
                                      i.get("user").get("name"))

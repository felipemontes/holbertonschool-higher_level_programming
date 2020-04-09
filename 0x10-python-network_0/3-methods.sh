#!/bin/bash
# sends a get request and shows body
curl -sI "$1" | grep Allow: | cut -d ':' -f2 | xargs

#!/bin/bash
# curl size of a body
curl -sI "$1" | grep Content-Length: | cut -d ' ' -f2

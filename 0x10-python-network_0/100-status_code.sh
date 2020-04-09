#!/bin/bash
# return only status code
curl -so /dev/null -w "%{http_code}" "$1"

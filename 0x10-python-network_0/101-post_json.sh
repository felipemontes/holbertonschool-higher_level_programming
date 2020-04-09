#!/bin/bash
#curl a json file
curl "$1" -Xs POST -H "Content-Type: application/json" -d "@$2"

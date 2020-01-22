#!/usr/bin/python3
import sys
import os


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file
newlist = []
leng = len(sys.argv) - 1

if os.path.exists("add_item.json"):
    newlist = load("add_item.json")

for i in range(leng):
    newlist.append(sys.argv[i + 1])

save(newlist, 'add_item.json')

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keys in a_dictionary.keys():
        if key == keys:
            a_dictionary[keys] = value
    a_dictionary[key] = value
    return a_dictionary

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for keys in a_dictionary.keys():
        if value == a_dictionary[keys]:
            a_dictionary.pop(keys)
    return a_dictionary

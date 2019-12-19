#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = dict(a_dictionary)
    for keys, value in new_d.items():
        new_d[keys] = value * 2
    return new_d

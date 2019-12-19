#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    new_l = my_list[:]
    res = list(map(lambda x: x * number, new_l))
    return res

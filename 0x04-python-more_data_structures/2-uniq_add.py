#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    new = list(s)
    res = 0
    for num in new:
        res += num
    return res

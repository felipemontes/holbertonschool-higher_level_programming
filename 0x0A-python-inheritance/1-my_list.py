#!/usr/bin/python3
class MyList(list):
    """ function to print a sorted list"""
    def print_sorted(self):
        newlist = []
        for i in self:
            newlist.append(i)
            newlist.sort()
        print(newlist)

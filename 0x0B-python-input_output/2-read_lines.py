#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ function to read n lines"""
    with open(filename) as f:
        if nb_lines <= 0:
            fl = f.read()
        else:
            fl = f.readline(nb_lines)
    print(fl, end="")

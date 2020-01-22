#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ function to read n lines"""
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines <= 0:
            fl = f.read()
            print(fl, end='')
        else:
            lines = 0
            for line in f:
                print(line, end='')
                lines += 1
                if lines == nb_lines:
                    break

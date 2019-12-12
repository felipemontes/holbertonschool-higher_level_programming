#!/usr/bin/python3
if __name__ == "__main__":
    from sys import *
    i = 1
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        while i < len(argv):
            print("{}: {}".format(i, argv[i]))
            i += 1

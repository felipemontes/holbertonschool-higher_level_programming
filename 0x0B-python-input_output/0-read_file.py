#!/usr/bin/python3
def read_file(filename=""):
    """function to read and print a file"""
    with open(filename, encoding="utf-8") as f:
        fil = f.read()
    print(fil, end="")

#!/usr/bin/python3
def append_write(filename="", text=""):
    """function to append a string"""
    with open(filename, "a") as f:
        nl = f.write(text)
    return nl

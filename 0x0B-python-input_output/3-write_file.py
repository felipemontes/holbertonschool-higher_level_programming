#!/usr/bin/python3
def write_file(filename="", text=""):
    """function to write in a file"""
    with open(filename, "w") as f:
        nl = f.write(text)
    return nl

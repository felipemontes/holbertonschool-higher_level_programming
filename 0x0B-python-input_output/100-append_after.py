#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """ functio to append afert certain line"""
    line = ''
    with open(filename, 'r+') as f:
        for words in f:
            line += words
            if search_string in words:
                line += new_string
        f.seek(0)
        f.write(line)

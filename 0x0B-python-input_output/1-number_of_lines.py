#!/usr/bin/python3
def number_of_lines(filename=""):
    """ function to count lines"""
    count = 0

    with open(filename) as f:
        for line in f:
            count += 1
    return count

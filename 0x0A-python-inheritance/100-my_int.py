#!/usr/bin/python3


class MyInt(int):
    """ class to invert operations"""

    def __eq__(int, other):
        return False

    def __ne__(int, other):
        return True

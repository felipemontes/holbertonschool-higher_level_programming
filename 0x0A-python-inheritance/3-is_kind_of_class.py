#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ function to check class and inhereit"""
    if isinstance(obj, a_class) and issubclass(obj.__class__, a_class):
        return True
    else:
        return False

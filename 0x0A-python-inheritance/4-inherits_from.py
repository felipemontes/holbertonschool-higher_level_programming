#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ function to check inheritance """
    if isinstance(obj, a_class) and issubclass(a_class, obj.__class__):
        return False
    else:
        return True

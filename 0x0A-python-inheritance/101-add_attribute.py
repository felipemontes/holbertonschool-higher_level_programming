#!/usr/bin/python3
def add_attribute(obj, name, attr):
    """function to check attributes"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, attr)
    else:
        raise TypeError('can\'t add new attribute')

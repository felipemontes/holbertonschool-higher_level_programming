#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    res = 0
    try:
        res = fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
    return res if res else None

#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        l = None
    else:
        l = len(sentence)
    f = sentence[0]
    res = (l, f)
    return res

#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    f = sentence[0]
    if l == 0:
        res(l, None)
    else:
        res = (l, f)
    return res

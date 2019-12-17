#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)

    if l == 0:
        res = (l, None)
    else:
        res = (l, sentence[0])
    return res

#!/usr/bin/python3
""" peak search """


def find_peak(ls):
    if ls:
        leng = len(ls)
        peak = ls[0]
        if ls[0] > ls[1]:
            peak = ls[0]
        for i in range(len(ls) - 1):
            if ls[i] > ls[i - 1] and ls[i] > ls[i + 1]:
                peak = ls[i]
        return peak
    else:
        return None

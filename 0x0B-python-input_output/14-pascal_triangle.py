#!/usr/bin/python3
def pascal_triangle(n):
    l = []
    conc = []

    for i in range(0, n):
        pos = l

        if i is not 0:
            l = [1]
        for b in range(1, i):
            l.append(pos[b - 1] + pos[b])
        l.append(1)
        conc.append(l)
    return conc

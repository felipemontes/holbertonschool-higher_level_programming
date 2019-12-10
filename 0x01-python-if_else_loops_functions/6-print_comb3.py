#!/usr/bin/python3
for i in range(0, 10):
    for b in range(i + 1, 10):
        print("{:d}{:d}".format(i, b), end='')
        if i == 8 and b == 9:
            pass
        else:
            print(", ", end='')
print("")

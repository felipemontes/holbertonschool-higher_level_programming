#!/usr/bin/python3
for ch in range(90, 64, -1):
    print("{}".format(chr(ch + 32)) if ch % 2 == 0 else "{}".format(chr(ch)),
          end='')

#!/usr/bin/python3
def uppercase(str):
    res = ''
    for char in str:
        char = ord(char)
        if char >= 97 and char < 123:
            res += chr(char - 32)
        elif char >= 65 and char <= 90:
            res += chr(char)
        elif char >= 48 and char <= 67:
            res += chr(char)
        elif char == 32:
            res += chr(char)
    print("{}".format(res))
    return res

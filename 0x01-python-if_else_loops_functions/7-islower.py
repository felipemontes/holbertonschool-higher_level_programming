def islower(c):
    b = ord(c)
    for i in range(97, 123):
        if i == b:
            return True
    return False

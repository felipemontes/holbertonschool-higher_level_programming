#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for dirs in dir(hidden_4):
        if dirs[0] == "_":
            pass
        else:
            print(dirs)

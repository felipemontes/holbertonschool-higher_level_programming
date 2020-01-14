#!/usr/bin/python3
def text_indentation(text):
    """ function to print a text """
    remp = ['?', '.', ':']
    new_str = ''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if text[i] is ' ' and text[i - 1] in remp:
            continue
        print(text[i], end='')
        if text[i] in remp:
            print('\n')

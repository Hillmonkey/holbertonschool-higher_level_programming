#!/usr/bin/python3
'''
module: 5-text_indentation
'''


def text_indentation(text):
    '''break text into lines on punctuation marks

    text: a big (maybe) of text to be broken into pieces ...
    '''

    # TEST/INPUT VALIDATION #
    if type(text) != str:
        raise TypeError("text must be a string")

    delims = {".", "?", ":"}
    new_line = False
    for ch in text:
        if ch in delims:
            print("{}\n".format(ch))
            new_line = True
        else:
            if not(new_line and ch == ' '):
                print(ch, end='')
            new_line = False

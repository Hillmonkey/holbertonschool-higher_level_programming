#!/usr/bin/python3


def multiple_returns(sentence):
    ''' returns tuple:
    first el: length of sentence
    second el: first char of sentence
    '''

    if sentence is None or len(sentence) == 0:
        return (0, None)
    first_char = sentence[0]

    return (len(sentence), first_char)

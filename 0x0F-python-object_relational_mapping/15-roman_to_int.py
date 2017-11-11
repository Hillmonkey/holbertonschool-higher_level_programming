#!/usr/bin/python3
'''module: 15-roman_to_int
'''


def roman_to_int(roman_string):
    '''function: roman_to_int
    accepts: string representation of roman number (all uppercase) (1 - 3,999)
    returns: an int
    If the roman_string is not a string or None, return 0
    '''
    roms = {"M": 0, "D": 1, "C": 2, "L": 3, "X": 4, "V": 5, "I": 6}
    ints = [1000, 500, 100, 50, 10, 5, 1]

    total = 0

    if roman_string is None or type(roman_string) != str:
        return 0

    prev = roms[roman_string[0]]
    total = ints[prev]
    for i, roman_char in enumerate(roman_string[1:]):
        this = roms[roman_char]
        if this >= prev:
            total += ints[roms[roman_char]]
        else:
            a = ints[roms[roman_char]]
            b = -2 * (ints[roms[roman_string[i]]])
            total += a + b
        prev = this
    return total

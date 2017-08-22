#!/usr/bin/python3


class Square:
    '''Class Square
    '''
    pass

    def __init__(self, size=0):
        '''init method of class Square
        '''
        try:
            self.__size = size
            if size < 0:
                raise ValueError

        except TypeError:
            print("size must an integer")
        except ValueError:
            print("size must be >= 0")

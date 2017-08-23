#!/usr/bin/python3
''' this comment takes up one line '''


class MagicClass:
    ''' class: MagicClass  cuz it is
    '''

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        ''' area '''
        return self.__radius**2 * math.pi

    def circumfrence(self):
        '''circumfrence'''
        return 2 * math.pi * self.__radius

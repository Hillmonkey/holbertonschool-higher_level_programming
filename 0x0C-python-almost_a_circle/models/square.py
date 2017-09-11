#!/usr/bin/python3
''' module: square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class: Square
    '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' method: __init__
        '''
        self.__width = size
        self.__height = size
        super().__init__(self.__width, self.__height, x, y, id)

    def __str__(self):
        ''' method: __str__ (of Square class)
        '''
        return ("[Square] ({} {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

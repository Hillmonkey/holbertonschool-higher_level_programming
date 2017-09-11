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
        # self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        '''method: size setter
        '''
        super().integer_GT_zero("width", size)
        self.width = size
        self.height = size

    def __str__(self):
        ''' method: __str__ (of Square class)
        '''
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

#!/usr/bin/python3
''' module: square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class: Square
    '''
    key_list = ['id', 'size', 'x', 'y']
    KV_dict = {'id': 'id', 'width': '_Rectangle__width',
               'height': '_Rectangle__height',
               'x': '_Rectangle__x', 'y': '_Rectangle__y'}
    KV_2 = {'id': 'id', '_Rectangle__width': 'width',
            '_Rectangle__height': 'height',
            '_Rectangle__x': 'x', '_Rectangle__y': 'y'}


    def __init__(self, size, x=0, y=0, id=None):
        ''' method: __init__
        '''
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

    def update(self, *args, **kwargs):
        '''method: update, Square class
        accepts variable length list of variables, updates attributes
        '''
        for idx, el in enumerate(args):  # handle args
            if idx != 1:
                self.__dict__[Square.KV_dict[Square.key_list[idx]]] = el
            else:  # deal with size
                self.height = el
                self.width = el
        if len(args) == 0:  # only handle kwargs if there are no args
            for key, val in kwargs.items():
                if key != "size":
                    self.__dict__[Square.KV_dict[key]] = val
                else:
                    self.height = val
                    self.width = val
    '''
    def to_dictionary(self):
        new_dict = {}
        for key, val in Square.KV_dict.items():
            new_dict[key] = self.__dict__[val]
        return new_dict
    '''

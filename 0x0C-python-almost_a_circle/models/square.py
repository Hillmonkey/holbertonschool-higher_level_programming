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
        key_list = ['id', 'size', 'x', 'y']
        KV_dict = {'id': 'id', 'width': '_Rectangle__width',
                   'height': '_Rectangle__height',
                   'x': '_Rectangle__x', 'y': '_Rectangle__y'}
        for idx, el in enumerate(args):  # handle args
            if idx != 1:
                self.__dict__[KV_dict[key_list[idx]]] = el
            else:  # deal with size
                self.height = el
                self.width = el
        if len(args) == 0:  # only handle kwargs if there are no args
            for key, val in kwargs.items():
                if key != "size":
                    self.__dict__[KV_dict[key]] = val
                else:
                    self.height = val
                    self.width = val

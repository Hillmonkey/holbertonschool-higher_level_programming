#!/usr/bin/python3
''' file/module base
'''


class Base:
    '''class: Base
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' method: __init__
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

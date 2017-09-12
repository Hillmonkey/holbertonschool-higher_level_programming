#!/usr/bin/python3
''' file/module base
'''
import json

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

    def to_json_string(list_dictionaries):
        ''' method: to_json_string
        accepts: list of dictionaries 
        returns: JSON representation as a string
        '''
        ret_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if type(list_dictionaries) != list:
            ret_list.append(list_dictionaries)
        else:
            ret_list = list_dictionaries
        return json.dumps(ret_list)
        

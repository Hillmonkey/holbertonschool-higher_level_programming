#!/usr/bin/python3
''' module: 11-student
'''


class Student:
    '''class: student
    '''

    def __init__(self, first_name, last_name, age):
        '''method: __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''method: to_json
        '''
        return self.__dict__

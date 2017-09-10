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
            # print("DEBUG:__init__, else case")


class Rectangle(Base):
    '''class: Rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''method: __init__
        rectangle instantiator
        '''
        self.integer_GT_zero("width", width)
        self.integer_GT_zero("height", height)
        self.integer_GTE_zero("x", x)
        self.integer_GTE_zero("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def area(self):
        '''public_method: area
        returns area of rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''public method: display
        prints ascii respresentation of a rectangle to stdout
        '''
        for i in range(self.__height):
            print("#" * self.__width)

    def integer_GT_zero(self, name, value):
        '''public_method: integer_GT_zero
        validates value is int > zero
        name: always a string
        value: positive integer
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def integer_GTE_zero(self, name, value):
        '''public_method: integer_GTE_zero
        validates value is int >= zero
        name: always a string
        value: positive integer, or ZERO
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        ''' method: width getter
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''method: width setter
        '''
        # self.integer_GT_zero("width", width)
        # print("width.setter")
        # integer_GT_zero("width", width)
        self.__width = width

    @property
    def height(self):
        ''' method: height getter
        '''
        return self.height

    @height.setter
    def height(self, height):
        ''' method: height getter
        '''
        # integer_GT_zero("height", height)
        self.__height = height

    @property
    def x(self):
        ''' method: x getter
        '''
        return self.__x

    @x.setter
    def x(self, x):
        ''' method: x setter
        '''
        # integer_GTE_zero("x", x)
        self.__x = x

    @property
    def y(self):
        ''' method y getter
        '''
        return self.__y

    @y.setter
    def y(self, y):
        ''' method y setter
        '''
        # integer_GTE_zero("y", y)
        self.__y = y

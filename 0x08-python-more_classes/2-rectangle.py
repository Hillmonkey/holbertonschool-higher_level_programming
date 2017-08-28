#!/usr/bin/python3

'''module: 2-rectangle
this module contains the class Rectangle ...
'''


class Rectangle:
    '''class: Rectangle
    this is an empty class, further additions in subsequent assignments
    '''

    def __init__(self, width=0, height=0):
        '''method: __init__
        initialize instance of class Rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''method: set_width
        getter
        '''
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''method: set_width
        setter
        '''
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''method: set_height
        getter
        '''
        if (not isinstance(self.__height, int)) or isinstance(self.__height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''method: set_height
        setter
        '''
        if not isinstance(self.__height, int) or isinstance(self.__height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        '''method: area
        return area of rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''method: perimeter
        return perimeter of perimeter
        '''
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

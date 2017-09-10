#!/usr/bin/python3
''' file/module base
'''


class Base:
    '''class: Base
    '''

    _nb_objects = 0

    def __init__(self, id=None):
        ''' method: __init__
        '''
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
            # print("DEBUG:__init__, else case")


class Rectangle(Base):
    '''class: Rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''method: __init__
        rectangle instantiator
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def update(self, *args):
        ''' method: update
        accepts variable length list of variables, updates attributes
        '''
        RD = {0: self.id, 1: self._width, 2: self._height, 3: self._x,
              4: self._y}
        for idx, el in enumerate(args):

            print(RD[idx])
            RD[idx] = el
            print(RD[idx])
            
    def __str__(self):
        ''' method: __str__
        '''
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self._x, self._y,
                self._width, self._height))

    def area(self):
        '''public_method: area
        returns area of rectangle
        '''
        return self._width * self._height

    def display(self):
        '''public method: display
        prints ascii respresentation of a rectangle to stdout
        '''
        print("\n" * (self._y), end="")
        for i in range(self._height):
            print(" " * self._x + "#" * self._width)

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
        return self._width

    @width.setter
    def width(self, width):
        '''method: width setter
        '''
        self.integer_GT_zero("width", width)
        # print("width.setter")
        # integer_GT_zero("width", width)
        self._width = width

    @property
    def height(self):
        ''' method: height getter
        '''
        return self.height

    @height.setter
    def height(self, height):
        ''' method: height getter
        '''
        self.integer_GT_zero("height", height)
        self._height = height

    @property
    def x(self):
        ''' method: x getter
        '''
        return self._x

    @x.setter
    def x(self, x):
        ''' method: x setter
        '''
        self.integer_GTE_zero("x", x)
        self._x = x

    @property
    def y(self):
        ''' method y getter
        '''
        return self._y

    @y.setter
    def y(self, y):
        ''' method y setter
        '''
        self.integer_GTE_zero("y", y)
        self._y = y

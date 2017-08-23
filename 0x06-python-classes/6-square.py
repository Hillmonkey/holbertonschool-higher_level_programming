#!/usr/bin/python3


class Square:
    '''Class Square
    '''
    pass

    def __init__(self, size=0, position=(0, 0)):
        '''init method of class Square
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2

    def my_print(self):
        err_msg = "position must be a tuple of 2 positive integers"
        if self.__position is None:
            self.__position = (0, 0)
        if type(self.__position) != tuple or len(self.__position) != 2:
            self.__position = (0, 0)
        if type(self.__position[0]) != int or type(self.__position[1]) != int:
            self.__position = (0, 0)
        if self.__position[0] < 0 or self.__position[1] < 0:
            self.__position = (0, 0)
        if self.__size == 0:
            print()
            return
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        err_msg = "position must be a tuple of 2 positive integers"
        if value is None:
            self.__position = (0, 0)
            raise TypeError(err_msg)
        if type(value) != tuple or len(value) != 2:
            self.__position = (0, 0)
            raise TypeError(err_msg)
        if type(value[0]) != int or type(value[1]) != int:
            self.__position = (0, 0)
            raise TypeError(err_msg)
        if value[0] < 0 or value[1] < 0:
            self.__position = (0, 0)
            raise TypeError(err_msg)
        self.__position = value

if __name__ == "__main__":
    for el in dir(Square):
        print(el)

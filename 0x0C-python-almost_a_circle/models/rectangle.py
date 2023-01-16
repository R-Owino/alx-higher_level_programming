#!/usr/bin/python3
'''Defines a class rectangle'''

Base = __import__("base").Base


class Rectangle(Base):
    '''Defines a Rectangle, derived class of Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor, initializes a new rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x: an atrribute
            y: an attribute
            id(int): a public instance attribute

        Raises:
            TypeError: width/height is not int
            ValueError: - width/height is less or equal to 0
                        - x/y is less than 0
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            '''sets/gets the width of the rectangle'''
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            '''Sets/gets the height of the rectangle'''
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            '''Sets/gets the x attribute of the rectangle'''
            return self.__x

        @x.setter
        def x(self, value):
            if type(x) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            '''Sets/gets the y attribute of the rectangle'''
            return self.__y

        @y.setter
        def y(self, value):
            if type(y) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

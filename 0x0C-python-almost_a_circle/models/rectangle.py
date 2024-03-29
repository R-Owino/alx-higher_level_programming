#!/usr/bin/python3
'''Defines a class Rectangle'''

from models.base import Base


class Rectangle(Base):
    '''Class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class constructor, initialize a new Rectangle.
        Args:
            width(int): width of the new Rectangle
            height(int): height of the new Rectangle
            x(int): an attribute of the Rectangle
            y(int): an attribute of the Rectangle
            id(int): public instance attribute

        Raises:
            TypeError if: - width or height is not an int
                          - x or y is not int
            ValueError if: - width or height <= 0
                           - x or y < 0
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Sets/gets the width of the Rectangle'''
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
        '''Sets/gets the height of the Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Sets/gets the x attribute'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''sets/gets the y attribute'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Returns area of the new Rectangle instance'''
        return self.__width * self.__height

    def display(self):
        '''prints the rectangle'''
        if self.width == 0 or self.height == 0:
            return ('')

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
            returns a string formart of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''overrides the __str__ method and updates the rectangle

        Args:
            *args(int): arguments id, width, height, x and y in that order
            **kwargs(dict): key/value pair of attributes
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''Returns the dict rep'n of a Rectangle'''

        return {'id': getattr(self, "id"),
                'width': getattr(self, "width"),
                'height': getattr(self, "height"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}

#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("*"*20)
print(my_rectangle)
print("*"*20)
print(repr(my_rectangle))
print("*"*20)
print(hex(id(my_rectangle)))
print("*"*20)

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("*"*20)
print(new_rectangle)
print("*"*20)
print(repr(new_rectangle))
print("*"*20)
print(hex(id(new_rectangle)))
print("*"*20)

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

from math import pi

def sqFoot():
    a = int(input('What is the length of your house? '))
    b = int(input('What is the width of your house? '))
    return f'The square footage of a house of length {a} and width {b} is {a*b} sq feet'

def circumference():
    r = input('What is the radius of the circle? ')
    return f'The circumference of a circle of radius {r} is {round(2 * pi * float(r), 2)}'
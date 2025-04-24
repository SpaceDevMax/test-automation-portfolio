import math

def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative")
    return length * width


def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2



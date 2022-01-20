# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
from math import pi
class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        return rectangle_area
    
    def perimeter(self):
        rectangle_perimeter = self.length*2 + self.width*2
        return rectangle_perimeter
    
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        circle_area = self.radius **2 * pi
        return circle_area
    
    def perimeter(self):
        circle_perimeter = self.radius *2 * pi
        return circle_perimeter

i = Circle(10)
print(f"The area of circle is {i.area()} and the perimeter is {i.perimeter()}")
    
r = Rectangle(10, 20)
print(f"The area of rectangle is {r.area()} and the perimeter is {r.perimeter()}")
    
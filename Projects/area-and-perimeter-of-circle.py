from math import pi

input_radius = int(input("Circle radius (cm): "))
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("Area is ", pi * self.radius ** 2, "cm2")
    def perimeter(self):
        print("Perimeter is ", 2 * pi * self.radius, "cm")

a = circle(input_radius)
a.area()
a.perimeter()
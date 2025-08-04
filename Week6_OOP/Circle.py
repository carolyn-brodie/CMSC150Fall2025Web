import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"


class Cylinder:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def volume(self):
        return self.base.area() * self.height

    def __str__(self):
        return f"Cylinder with base {self.base} and height {self.height}"


def tester():
    c1 = Circle(5)
    # print(c1)
    # print(f"Area is {c1.area()}")
    # print(f"Circumference is {c1.circumference()}")
    cyl1 = Cylinder(c1, 10)
    print(cyl1)
    print(f"Volume is {cyl1.volume()}")


if __name__ == "__main__":
    tester()
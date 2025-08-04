

class Triangle:
    """
    2.	Write a class to represent a Triangle.  The triangle has two attributes,
    the length of the base and the length of the height.                                                                                                         (5 points)
a.	Make sure that the Triangle class contains a constructor and a __str__ method
so that it can be printed.
b.	Add a method that calculates the area of the triangle (1/2 * base * height).
The method should not take any formal parameters besides self and should
return the area.

    """

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return f"Triangle with base {self.base} and height {self.height}"

    def area(self):
        return (1/2) * self.base * self.height

class Prism:
    """
    3.	Write a class to represent a Prism.  The prism has two attributes,
    the shape of the base and the height.
    a.	Make sure that the Prism class contains a constructor and a __str__ method"""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return f"Prism with base {self.base} and height {self.height}"

    def volume(self):
        return self.base.area() * self.height


def tester():
    t1 = Triangle(5, 10)
    # print(t1)
    # print(f"Area is {t1.area()}")
    p1 = Prism(t1, 10)
    print(p1)
    print(f"Volume is {p1.volume()}")


if __name__ == "__main__":
    tester()
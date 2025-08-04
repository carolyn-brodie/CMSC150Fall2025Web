
## calculate the area of a slice of pizza

import math

radius = input("Enter the radius of the pizza: ")
radius = int(radius)
number_of_slices = int(input("Enter the number of slices: "))
print((math.pi * (radius ** 2)) / number_of_slices)
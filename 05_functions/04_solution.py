import math

def circle_stats(radius):
    area = round(math.pi * radius ** 2)
    circumference = round(2 * math.pi * radius)
    return(area, circumference)

a, b = circle_stats(3)

print("Area: ", a, "Circumference: ", b)
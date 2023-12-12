import math


def table(points, f):
    for x in points:
        print(f"{x:6.2f} - {f(x)}")
from math import pi, sin,cos,tan
# pts = [math.pi / 2 * i / 4 for i in range(5)]
pts = [0, pi/6, pi/4, pi/3, pi/2]
# print(*pts)

table(pts, sin)
table(pts, tan)
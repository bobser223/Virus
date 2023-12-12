x, y = [float(d) for d in input().split()]
import math
r=(y**2-x/math.pi)**0.5
print(f"{r: 0.2f}")
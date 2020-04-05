import math

a, b, x = map(int, input().split())
if a ** 2 * b / 2 <= x:
    f = 2 * (a ** 2 * b - x) / a ** 3
    print(math.degrees(math.atan(f)))
else:
    f = 2 * x / (b ** 2 * a)
    print(90 - math.degrees(math.atan(f)))
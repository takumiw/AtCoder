import math
H = int(input())

p = math.floor(math.log2(H))
print(2 ** (p + 1) - 1)
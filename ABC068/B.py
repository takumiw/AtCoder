import math
n = int(input())
for i in range(n, 0, -1):
    if math.log2(i).is_integer():
        print(i)
        exit()
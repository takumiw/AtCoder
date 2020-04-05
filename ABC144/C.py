import numpy as np
N = int(input())

for i in range(int(np.sqrt(N)), 0, -1):
    if N % i == 0:
        break

a1, a2 = i, N//i

print(a1 + a2 - 2)
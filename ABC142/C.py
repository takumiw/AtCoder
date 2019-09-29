import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
B = np.argsort(A)
for b in B:
    print(b+1, end=' ')
print()
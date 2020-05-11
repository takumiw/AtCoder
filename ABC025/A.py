from itertools import product
def pro(l, n):
    return list(product(l, repeat=n))

S = input()
N = int(input())
print(''.join(pro(list(S), 2)[N-1]))
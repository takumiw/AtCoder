import math
from itertools import permutations
N = int(input())
TOWNS = [tuple(map(int, input().split())) for _ in range(N)]

cands = [p for p in permutations([i for i in range(0, N)], N)]
s = 0
for cand in cands:
    for i in range(N-1):
        start = TOWNS[cand[i]]
        dist = TOWNS[cand[i+1]]
        s += math.sqrt((start[0] - dist[0])**2 + (start[1] - dist[1])**2)

print(s / math.factorial(N))
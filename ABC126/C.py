import math
N, K = map(int, input().split())

ans = 0
for n in range(1, N+1):
    if n >= K:
        ans += 1
        continue
    ans += (1/2) ** math.ceil(math.log2(K / n))

print(ans / N)
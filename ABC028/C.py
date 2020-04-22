from itertools import combinations
a, b, c, d, e = map(int, input().split())
ans = [sum(p) for p in combinations([a, b, c, d, e], 3)]
ans.sort()
print(ans[-3])
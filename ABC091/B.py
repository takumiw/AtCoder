N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

ans = 0
for s in set(S):
    ans = max(ans, S.count(s) - T.count(s))

print(ans)
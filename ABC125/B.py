N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
XY = [v - c for v, c in zip(V, C) if v - c >= 0]

ans = sum(XY)
print(ans)
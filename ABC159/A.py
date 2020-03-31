N, M = map(int, input().split())

ans = N * (N-1) / 2
ans += M * (M-1) / 2

print(int(ans))
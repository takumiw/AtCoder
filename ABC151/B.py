N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = M * N - sum(A)
if ans > K:
    print(-1)
else:
    print(max(0, ans))
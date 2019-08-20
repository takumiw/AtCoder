N = int(input())
W = list(map(int, input().split()))

min_diff = sum(W)
for i in range(1, N):
    min_diff = min(min_diff, abs(sum(W[:i]) - sum(W[i:])))

print(min_diff)
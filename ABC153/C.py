from heapq import heapify, heappush, heappop
N, K = map(int, input().split())
H = list(map(int, input().split()))

H = [-h for h in H]
heapify(H)
for _ in range(K):
    if len(H) == 0:
        break
    heappop(H)

print(-sum(H))
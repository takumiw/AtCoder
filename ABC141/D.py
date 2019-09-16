from heapq import heapify, heappush, heappop
import math

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [-a for a in A]
    heapify(A)

    while M:
        # heapqの最小値をpopする
        m = heappop(A)
        heappush(A, math.ceil(m/2))
        M -= 1
    print(-sum(A))

if __name__ == '__main__':
    solve()
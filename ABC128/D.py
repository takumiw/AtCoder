import sys
readline = sys.stdin.readline
from heapq import heapify, heappush, heappop

def main():
    N, K = map(int, readline().rstrip().split())
    V = list(map(int, readline().rstrip().split()))
    V_rev = V[::-1]
    res = 0
    for x in range(min(N, K)+1):
        for y in range(min(N, K)-x+1):
            z = K - x - y
            temp = V[:x] + V_rev[:y]
            heapify(temp)
            for _ in range(z):
                if temp:
                    m = heappop(temp)
                    if m >= 0:
                        heappush(temp, m)
                        break
                else:
                    break

            res = max(res, sum(temp))
    
    print(res)


if __name__ == '__main__':
    main()
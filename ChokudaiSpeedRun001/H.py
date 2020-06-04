import sys
readline = sys.stdin.readline
from bisect import bisect_left
INF = 10 ** 10


def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    dp = [INF for _ in range(N)]
    res = 0
    
    for a in A:
        i = bisect_left(dp, a)
        dp[i] = a
        res = max(res, i)
    
    print(res + 1)


if __name__ == "__main__":
    main()

import sys
readline = sys.stdin.readline
INF = 10 ** 10


def main():
    N, M = map(int, readline().rstrip().split())
    C = list(map(int, readline().rstrip().split()))
    dp = [INF] * (N + 1)
    dp[0] = 0
    for c in C:
        for i in range(c, N+1):
            dp[i] = min(dp[i], dp[i-c] + 1)
    
    print(dp[N])


if __name__ == '__main__':
    main()
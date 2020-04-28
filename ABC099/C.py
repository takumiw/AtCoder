import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    dp = [i for i in range(N+1)]

    for i in range(N):
        dp[i+1] = min(dp[i+1], dp[i]+1)
        e = 9
        while i + e <= N:
            dp[i+e] = min(dp[i+e], dp[i]+1)
            e *= 9
        e = 6
        while i + e <= N:
            dp[i+e] = min(dp[i+e], dp[i]+1)
            e *= 6

    print(dp[N])


if __name__ == '__main__':
    main()
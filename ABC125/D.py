import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    dp = [[0, 0] for _ in range(N+1)]
    dp[0][1] = - 10 ** 10
    for i in range(N):
        dp[i+1][0] = max(dp[i][0] + A[i], dp[i][1] - A[i])
        dp[i+1][1] = max(dp[i][0] - A[i], dp[i][1] + A[i])

    print(dp[N][0])

if __name__ == '__main__':
    main()
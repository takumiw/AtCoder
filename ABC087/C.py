import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A1 = list(map(int, readline().rstrip().split()))
    A2 = list(map(int, readline().rstrip().split()))
    dp = [[0, 0]  for _ in range(N)]
    dp[0][0] = A1[0]
    dp[0][1] = A1[0] + A2[0]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + A1[i]
        dp[i][1] = max(dp[i-1][1], dp[i][0]) + A2[i]

    print(dp[N-1][1])

if __name__ == '__main__':
    main()
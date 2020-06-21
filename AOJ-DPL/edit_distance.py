import sys
readline = sys.stdin.readline


def main():
    S = readline().rstrip()
    T = readline().rstrip()

    N, M = len(S), len(T)
    dp = [[0] * (M+1) for _ in range((N+1))]
    dp[0] = [i for i in range(M+1)]
    for i in range(N+1):
        dp[i][0] = i
    
    for i, s in enumerate(S):
        for j, t in enumerate(T):
            if s == t:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1

    print(dp[N][M])


if __name__ == '__main__':
    main()
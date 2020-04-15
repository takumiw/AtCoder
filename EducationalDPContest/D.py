def main():
    N, W = map(int, input().split())
    dp = [[0] * (W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        w, v = map(int, input().split())
        dp_pre = dp[i-1]
        for j in range(w):
            dp[i][j] = dp_pre[j]
        for j in range(w, W+1):
            dp[i][j] = max(dp_pre[j-w] + v, dp_pre[j])

    print(max(dp[N]))


if __name__ == "__main__":
    main()
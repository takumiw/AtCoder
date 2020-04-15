INF = 10 ** 9 + 1
MAV_V = 10 ** 5 + 1

def main():
    N, W = map(int, input().split())
    dp = [[INF] * MAV_V for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        w, v = map(int, input().split())
        pre_dp = dp[i-1]
        for j in range(v):
            dp[i][j] = min(pre_dp[j], w)
        for j in range(v, MAV_V):
            if pre_dp[j-v] + w <= W:
                dp[i][j] = min(pre_dp[j-v] + w, pre_dp[j])
            else:
                dp[i][j] = pre_dp[j]

    ans = [i for i, v in enumerate(dp[-1]) if v != INF]
    print(max(ans))


if __name__ == "__main__":
    main()
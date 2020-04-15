INF = 10 ** 9

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    dp = [INF] * N
    dp[0] = 0
    for i in range(1, N):
        ks = max(0, i-K)
        hi = H[i]
        for j in range(ks, i):
            dp[i] = min(dp[i], dp[j] + abs(hi - H[j]))
    
    print(dp[N-1])


if __name__ == "__main__":
    main()
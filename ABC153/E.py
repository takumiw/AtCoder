INF = 10 ** 9

def main():
    H, N = map(int, input().split())

    dp = [INF] * (H+1)
    dp[0] = 0
    for _ in range(N):
        a, b = map(int, input().split())
        for j in range(H):
            nj = min(j+a, H)
            dp[nj] = min(dp[nj], dp[j]+b)

    print(dp[H])


if __name__ == "__main__":
    main()
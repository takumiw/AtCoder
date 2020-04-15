def main():
    N = int(input())
    a1, b1, c1 = map(int, input().split())
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = [a1, b1, c1]
    
    for i in range(1, N):
        a, b, c = map(int, input().split())
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a
        dp[i][1] = max(dp[i-1][2], dp[i-1][0]) + b
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c
    
    print(max(dp[N-1]))


if __name__ == "__main__":
    main()
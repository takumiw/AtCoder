def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            p = (S[i-1] == T[j-1])
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + p)
            
    ans = []
    x, y = N, M
    while x and y:
        if dp[x][y] == dp[x-1][y]:
            x -= 1
        elif dp[x][y] == dp[x][y-1]:
            y -= 1
        else:
            x -= 1
            y -= 1
            ans.append(S[x])
        
    print(''.join(reversed(ans)))


if __name__ == "__main__":
    main()
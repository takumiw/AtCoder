import sys
readline = sys.stdin.readline

def main():
    N, L = map(int, readline().rstrip().split())
    X = list(map(int, readline().rstrip().split()))
    is_hurdle = [False] * (L+1)
    for x in X:
        is_hurdle[x] = True
    T = tuple(map(int, readline().rstrip().split()))

    dp = [0] * (L+1)
    dp[1] = T[0]
    if is_hurdle[1]:
        dp[1] += T[2]

    for i in range(2, min(4, L+1)):
        dp[i] = min(dp[i-1], dp[i-2] + T[1]) + T[0]
        if is_hurdle[i]:
            dp[i] += T[2]
    
    for i in range(4, L+1):
        dp[i] = min(dp[i-1], dp[i-2] + T[1], dp[i-4] + 3 * T[1]) + T[0]
        if is_hurdle[i]:
            dp[i] += T[2]
    
    if L == 2:
        print(min(dp[L], dp[L-1] + T[0]//2 + T[1]//2, dp[L-2] + T[0]//2 + (T[1] * 3) // 2))
    else:
        print(min(dp[L], dp[L-1] + T[0]//2 + T[1]//2, dp[L-2] + T[0]//2 + (T[1] * 3) // 2, dp[L-3] + T[0]//2 + (T[1] * 5) // 2))

if __name__ == '__main__':
    main()
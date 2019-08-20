import sys
input = sys.stdin.readline
MOD = 10**9 + 7

def main():
    N, M = map(int, input().split())
    broken_floors = set(int(input()) for _ in range(M))
    dp = [0]*(N+2)
    dp[1] = 1

    for i in range(1, N+1):
        if i not in broken_floors:
            dp[i+1] = (dp[i] + dp[i-1]) % MOD

    print(dp[-1])

if __name__ == '__main__':
    main()
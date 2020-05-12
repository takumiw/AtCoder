import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7

def main():
    S = readline().rstrip()
    N = 13
    dp = [0] * 13  # dp[k]: 13で割った余りがkのパターン数
    dp[0] = 1
    
    mul = 1
    for s in S[::-1]:
        next_dp = [0] * N
        if s == '?':
            for k in range(10):
                for j in range(N):
                    next_dp[(k * mul + j) % N] += dp[j]
                    next_dp[(k * mul + j) % N] %= MOD
        else:
            k = int(s)
            for j in range(N):
                next_dp[(k * mul + j) % N] += dp[j]
                next_dp[(k * mul + j) % N] %= MOD
        mul *= 10
        mul %= N
        dp = next_dp

    print(dp[5])

if __name__ == '__main__':
    main()
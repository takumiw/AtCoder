import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7

def factorial(N, mod=MOD):
    res = 1
    for i in range(2, N+1):
        res *= i
        res %= mod
    return res

def main():
    N, M = map(int, readline().rstrip().split())
    if abs(N-M) > 1:
        ans = 0
    elif N == M:
        ans = factorial(N) ** 2 * 2
    else:
        ans = factorial(min(N, M)) ** 2 * max(N, M)

    print(ans % MOD)


if __name__ == '__main__':
    main()
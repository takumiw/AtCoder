import sys
readline = sys.stdin.buffer.readline
MOD = 10 ** 9 + 7

def main():
    N, K = map(int, readline().rstrip().split())
    ans = 0
    m = (N * (N + 1)) // 2
    for k in range(K, N+2):
        mi = ((k-1) * k) // 2
        ma = m - ((N-k) * (N-k+1)) // 2
        ans += (ma - mi + 1)

    print(ans % MOD)


if __name__ == '__main__':
    main()
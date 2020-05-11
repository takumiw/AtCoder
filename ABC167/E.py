import sys
readline = sys.stdin.readline
MOD = 998244353

N, M, K = map(int, readline().rstrip().split())
fact = [1] * (N+1)
finv = [1] * (N+1)
inv = [1] * (N+1)
inv[0] = 0
for i in range(2, N+1):
    fact[i] = (fact[i-1] * i % MOD)
    inv[i] = (-inv[MOD%i] * (MOD // i)) % MOD
    finv[i] = (finv[i-1] * inv[i]) % MOD

def comb(n, r, mod=MOD):
    if r < 0 or n < r:
        return 0
    return fact[n] * finv[r] * finv[n-r] % mod

def main():
    res = 0
    for k in range(K+1):
        res += comb(N-1, k, MOD) * pow(M-1, N-k-1, MOD) * M
        res %= MOD
    
    print(res)


if __name__ == '__main__':
    main()
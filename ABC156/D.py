n, a, b = map(int, input().split())
MOD = 10 ** 9 + 7

def comb(n,r, mod):
    res = 1
    fac = 1
    for i in range(r):
        res *= n-i
        res %= mod
        fac *= i+1
        fac %= mod
    return res * pow(fac, mod-2, mod) % mod

def main():
    ans = pow(2, n, MOD) - 1
    ans -= comb(n=n, r=a, mod=MOD)
    ans -= comb(n=n, r=b, mod=MOD)
    ans %= MOD
    print(ans)

if __name__ == "__main__":
    main()
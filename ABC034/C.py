import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7

# nCr % mod
def comb(n, r, mod=MOD):
    r = min(n - r, r)
    res = 1
    fac = 1
    for i in range(r):
        res *= n - i
        res %= mod
        fac *= i + 1
        fac %= mod
    return res * pow(fac, mod-2, mod) % mod

def main():
    W, H = map(int, readline().rstrip().split())
    W -= 1
    H -= 1
    print(comb((W+H), W))

if __name__ == '__main__':
    main()
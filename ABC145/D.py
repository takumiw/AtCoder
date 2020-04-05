from math import factorial
X, Y = map(int, input().split())
MOD = 10**9 + 7

def comb(n, r, p):
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)

    if r < 0 or n < r:
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % p

def solve():
    a = (2*Y-X) / 3
    b = (2*X-Y) / 3
    if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
        ans = comb(int(a+b), int(min(a, b)), MOD)
        print(ans)
    else:
        print(0)

if __name__ == '__main__':
    solve()
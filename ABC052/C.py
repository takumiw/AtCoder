import sys
readline = sys.stdin.readline
from collections import Counter
MOD = 10 ** 9 + 7

def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

def main():
    N = int(readline())
    factors = []
    for i in range(1, N+1):
        factors += factorize(i)
    c = Counter(factors)
    ans = 1
    for key, val in c.items():
        if key == 1:
            continue
        ans *= (val + 1)
        ans %= MOD
    
    print(ans)


if __name__ == '__main__':
    main()
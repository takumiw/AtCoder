import sys
readline = sys.stdin.readline

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

def main():
    N = int(readline())
    fct = factorize(N)
    res = 0
    for a, b in fct:
        p = 1
        while b - p >= 0:
            b -= p
            res += 1
            p += 1

    print(res)
    
if __name__ == '__main__':
    main()
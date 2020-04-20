import sys
readline = sys.stdin.readline
from math import factorial
MOD = 10 ** 9 + 7

def main():
    N, K = map(int, readline().rstrip().split())
    f1 = factorial(N-K+1)
    f2 = factorial(K-1)
    f3 = 1
    for i in range(1, K+1):
        if N - K + 1 - i < 0:
            print(0)
            continue
        ans = f2 // (f3 * factorial(K-i))
        f3 *= i
        ans *= f1 // (f3 * factorial(N-K+1-i))
        print(ans % MOD)


if __name__ == '__main__':
    main()
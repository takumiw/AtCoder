import sys
readline = sys.stdin.readline
import math

def count_factor(n, d=2):
    if n % d != 0:
        return 0
    for i in range(n):
        if n & d<<i:
            return i + 1

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))

    ans = sum([count_factor(a) for a in A])
    print(ans)

if __name__ == '__main__':
    main()
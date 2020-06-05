import sys
readline = sys.stdin.readline
# from math import gcd
from fractions import gcd

def main():
    N = int(readline())
    for _ in range(N):
        a, b = map(int, readline().rstrip().split())
        print(gcd(a, b))

if __name__ == '__main__':
    main()
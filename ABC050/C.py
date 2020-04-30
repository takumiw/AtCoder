import sys
readline = sys.stdin.readline
from collections import Counter
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    c = Counter(A)
    if N % 2 == 1:
        if c[0] != 1:
            print(0)
            return
        for i in range(2, N, 2):
            if c[i] != 2:
                print(0)
                return

    else:
        for i in range(1, N, 2):
            if c[i] != 2:
                print(0)
                return

    print(pow(2, N//2, MOD))

if __name__ == '__main__':
    main()
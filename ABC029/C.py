import sys
readline = sys.stdin.readline
from itertools import product


def main():
    N = int(readline())
    ans = product('abc', repeat=N)
    ans = [''.join(a) for a in ans]
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
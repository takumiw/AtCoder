import sys, math
sys.setrecursionlimit(10 ** 6)
from collections import deque, defaultdict, Counter
from operator import itemgetter

def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    print(len(set(D)))


if __name__ == '__main__':
    main()
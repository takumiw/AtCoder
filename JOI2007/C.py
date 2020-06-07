import sys
readline = sys.stdin.readline
from itertools import combinations_with_replacement
from bisect import bisect_left


def main():
    N, M = map(int, readline().rstrip().split())
    P = [int(readline()) for _ in range(N)]
    P.append(0)
    scr = [p1 + p2 for p1, p2 in combinations_with_replacement(P, 2) if p1 + p2 <= M]
    scr.sort()

    res = 0
    for p1 in scr:
        p = M - p1
        i = bisect_left(scr, p)
        p2 = scr[i - 1]
        res = max(res, p1 + p2)
    
    print(res)

if __name__ == '__main__':
    main()
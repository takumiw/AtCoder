import sys
readline = sys.stdin.readline
from operator import itemgetter
INF = 10 ** 10

def main():
    N = int(readline())
    L = []
    for _ in range(N):
        x, l = map(int, readline().rstrip().split())
        L.append([x - l, x + l])

    L.sort(key=itemgetter(1))
    cur = -INF
    res = 0

    for left, right in L:
        if left >= cur:
            res += 1
            cur = right
    
    print(res)

if __name__ == '__main__':
    main()
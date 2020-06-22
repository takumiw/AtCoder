import sys
readline = sys.stdin.readline
from collections import Counter


def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    counter = Counter(A)
    res = sum(A)

    Q = int(readline())
    for _ in range(Q):
        b, c = map(int, readline().rstrip().split())
        res = res - b * counter[b] + c * counter[b]
        counter.setdefault(c, 0)
        counter[c] += counter[b]
        counter.setdefault(b, 0)
        counter[b] = 0

        print(res)
        

if __name__ == '__main__':
    main()
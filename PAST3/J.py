import sys
readline = sys.stdin.readline
from bisect import bisect_right

def main():
    N, M = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    eat = [0] * N

    for a in A:
        i = bisect_right(eat, -a)
        if i >= N:
            print(-1)
            continue
        print(i + 1)
        eat[i] = -a


if __name__ == '__main__':
    main()
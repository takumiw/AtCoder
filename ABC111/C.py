import sys
from collections import Counter
sys.setrecursionlimit(10 ** 6)

def main():
    N = int(input())
    V = list(map(int, sys.stdin.readline().rstrip().split()))
    c0 = Counter([v for i, v in enumerate((V)) if i % 2 == 0])
    c1 = Counter([v for i, v in enumerate((V)) if i % 2 == 1])

    if c0.most_common()[0][0] == c1.most_common()[0][0]:
        if len(c0.most_common()) == 1:
            m = c1.most_common()[0][1]
            print(m)
        elif len(c1.most_common()) == 1:
            m = c0.most_common()[0][1]
            print(m)
        else:
            m = max(c0.most_common()[0][1] + c1.most_common()[1][1], c0.most_common()[1][1] + c1.most_common()[0][1])
            print(N - m)
    else:
        m = c0.most_common()[0][1] + c1.most_common()[0][1]
        print(N - m)


if __name__ == '__main__':
    main()
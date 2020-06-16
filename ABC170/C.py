import sys
readline = sys.stdin.readline


def main():
    X, N = map(int, readline().rstrip().split())
    P = set(map(int, readline().rstrip().split()))

    for i in range(200):
        if X - i not in P:
            print(X - i)
            return
        if X + i not in P:
            print(X + i)
            return


if __name__ == '__main__':
    main()
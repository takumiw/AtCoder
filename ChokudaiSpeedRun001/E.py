import sys

readline = sys.stdin.readline


def main():
    N = int(readline())
    l = list(map(int, readline().rstrip().split()))
    print(l.index(1) + 1)


if __name__ == "__main__":
    main()

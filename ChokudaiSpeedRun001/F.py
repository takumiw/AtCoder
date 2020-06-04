import sys

readline = sys.stdin.readline


def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    res = 0
    ma = A[0]
    for a in A[1:]:
        if a > ma:
            res += 1
        ma = max(ma, a)

    print(res + 1)


if __name__ == "__main__":
    main()

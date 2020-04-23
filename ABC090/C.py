import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    if N == 1 and M == 1:
        print(1)
        return
    if N == 1 or M == 1:
        print(max(N, M) - 2)
        return
    print((N-2) * (M-2))
    return


if __name__ == '__main__':
    main()
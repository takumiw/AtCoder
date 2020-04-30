import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    T = list(map(int, readline().rstrip().split()))
    S = sum(T)
    M = int(readline())
    for _ in range(M):
        p, x = map(int, readline().rstrip().split())
        print(S - T[p-1] + x)


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    L, H = map(int, readline().rstrip().split())
    N = int(readline())
    for _ in range(N):
        a = int(readline())
        if a > H:
            print(-1)
        else:
            print(max(0, L-a))


if __name__ == '__main__':
    main()
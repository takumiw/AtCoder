import sys
readline = sys.stdin.readline

def main():
    N, L = map(int, readline().rstrip().split())
    S = [readline().rstrip() for _ in range(N)]
    S.sort()
    print(*S, sep='')

if __name__ == '__main__':
    main()
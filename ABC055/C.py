import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    ans = min(N, M//2)
    M -= ans * 2
    ans += M//4
    print(ans)


if __name__ == '__main__':
    main()
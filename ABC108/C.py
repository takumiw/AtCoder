import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    if K % 2 == 1:
        p = N // K
        ans = p ** 3
    else:
        p = N // K
        ans = p ** 3
        p = (N + K//2) // K
        ans += p ** 3

    print(ans)

if __name__ == '__main__':
    main()
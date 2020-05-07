import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    H = [int(readline()) for _ in range(N)]
    H.sort()
    ans = 10 ** 10
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])

    print(ans)

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    N, T = map(int, readline().rstrip().split())
    A = [int(readline()) for _ in range(N)]
    ans = 0
    for i in range(N-1):
        ans += min(T, A[i+1] - A[i])

    print(ans+T)


if __name__ == '__main__':
    main()
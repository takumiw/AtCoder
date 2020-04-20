import sys
readline = sys.stdin.buffer.readline

def main():
    N, X = map(int, readline().rstrip().split())
    M = [int(readline()) for _ in range(N)]

    X -= sum(M)
    ans = N
    ans += X // min(M)
    print(ans)


if __name__ == '__main__':
    main()
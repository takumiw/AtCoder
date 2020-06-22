import sys
readline = sys.stdin.readline

def main():
    N, W = map(int, readline().rstrip().split())
    dp = [0] * (W + 1)

    for _ in range(N):
        v, w = map(int, readline().rstrip().split())
        for i in range(W, w-1, -1):
            dp[i] = max(dp[i], dp[i-w] + v)

    print(max(dp))

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline


def main():
    N, W = map(int, readline().rstrip().split())
    dp = [0] * (W + 1)

    for _ in range(N):
        v, w = map(int, readline().rstrip().split())
        for j in range(W-w+1):
            dp[j+w] = max(dp[j+w], dp[j] + v)

    print(dp[-1])


if __name__ == '__main__':
    main()
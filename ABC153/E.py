import sys
readline = sys.stdin.readline
INF = 10 ** 8


def main():
    H, N = map(int, readline().rstrip().split())
    dp = [INF] * (H + 1)  # HPを減らすのに必要な最小のMP
    dp[0] = 0

    for _ in range(N):
        hp, mp = map(int, readline().rstrip().split())

        for i in range(H):
            j = min(i+hp, H)
            dp[j] = min(dp[j], dp[i] + mp)

    print(dp[-1])


if __name__ == '__main__':
    main()
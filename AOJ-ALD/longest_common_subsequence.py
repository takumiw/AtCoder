import sys
readline = sys.stdin.readline


def main():
    N = int(readline())
    for _ in range(N):
        X = readline().rstrip()
        Y = readline().rstrip()

        len_x, len_y = len(X), len(Y)
        dp = [[0] * (len_y + 1) for _ in range(len_x + 1)]

        for i, x in enumerate(X):
            for j, y in enumerate(Y):
                if x == y:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        print(dp[len_x][len_y])


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline


def main():
    N, M = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    B = list(map(int, readline().rstrip().split()))

    dp = [[0] * (M+1) for _ in range(N+1)]  # dp[i][j] = 既にとった数が(i, j)の時の先攻のスコア

    for i in range(N, -1, -1):
        for j in range(M, -1, -1):
            if i + j == N + M:
                continue

            # 専攻の時は、2通りある内のよりスコアが大きくなる方へ行動
            if (i + j) % 2 == 0:
                # Bの山からしか取れない時
                if i == N:
                    dp[i][j] = B[j] + dp[i][j+1]
                # Aの山からしか取れない時
                elif j == M:
                    dp[i][j] = A[i] + dp[i+1][j]
                else:
                    dp[i][j] = max(A[i] + dp[i+1][j], B[j] + dp[i][j+1])
            
            # 後攻の時は、専攻のスコアが小さくなる様に行動する
            else:
                # Bの山からしか取れないとき
                if i == N:
                    dp[i][j] = dp[i][j+1]
                    #Aの山からしか取れないとき
                elif j == M:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1])

    print(dp[0][0])


if __name__ == '__main__':
    main()
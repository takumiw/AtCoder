import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    dp = [0] * N
    dp[1] = abs(A[1] - A[0])
    for i in range(2, N):
        dp[i] = min(dp[i-2] + abs(A[i] - A[i-2]), dp[i-1] + abs(A[i] - A[i-1]))
    print(dp[N-1])

if __name__ == '__main__':
    main()
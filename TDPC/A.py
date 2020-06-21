import sys
readline = sys.stdin.readline
INF = 10 ** 4

def main():
    N = int(readline())
    P = list(map(int, readline().rstrip().split()))
    dp = [False] * (INF + 1)
    dp[0] = True

    for p in P:
        for i in range(INF, p-1, -1):
            if dp[i-p]:
                dp[i] = True
    
    print(sum(dp))

if __name__ == '__main__':
    main()
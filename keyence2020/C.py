import sys
readline = sys.stdin.readline
INF = 10 ** 9

def main():
    N, K, S = map(int, readline().rstrip().split())
    if S < INF:
        res = [S] * K  + [INF] * (N - K)
    else:
        res = [S] * K + [1] * (N - K) 

    print(*res)

if __name__ == '__main__':
    main()
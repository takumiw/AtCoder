import sys
readline = sys.stdin.readline
INF = 10 ** 10

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, readline().rstrip().split())
        path[a-1][b-1] = t
        path[b-1][a-1] = t
    
    for i in range(N):
        path[i][i] = 0
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                path[i][j] = min(path[i][j], path[i][k] + path[k][j])
    
    res = INF
    for i in range(N):
        res = min(res, max(path[i]))

    print(res)

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline
from itertools import combinations
INF = 10 ** 10

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[INF]*(N) for _ in range(N)]
    
    for _ in range(M):
        u, v, l = map(int, readline().rstrip().split())
        path[u-1][v-1] = l
        path[v-1][u-1] = l

    for k in range(1, N):
        for i in range(1, N):
            for j in range(1, N):
                path[i][j] = min(path[i][j], path[i][k] + path[k][j])
    
    ans = INF
    neighbor = [i for i in range(N) if path[0][i] != INF]
    for s, g in combinations(neighbor, 2):
        ans = min(ans, path[s][g] + path[0][s] + path[g][0])

    if ans != INF:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()
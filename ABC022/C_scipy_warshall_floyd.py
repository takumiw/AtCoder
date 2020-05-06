import sys
readline = sys.stdin.readline
from itertools import combinations
from scipy.sparse.csgraph import floyd_warshall
INF = 10 ** 10

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[INF]*(N) for _ in range(N)]
    neighbor = {}
    for _ in range(M):
        u, v, l = map(int, readline().rstrip().split())
        if u == 1:
            neighbor[v-1] = l
        else:
            path[u-1][v-1] = l
            # path[v-1][u-1] = l

    G = floyd_warshall(path, directed=False)  # directed=False (i,j).(j,i)両方できるようになる
    ans = INF
    for s, g in combinations(neighbor.keys(), 2):
        ans = min(ans, G[s][g] + neighbor[s] + neighbor[g])

    if ans != INF:
        print(int(ans))
    else:
        print(-1)

if __name__ == '__main__':
    main()
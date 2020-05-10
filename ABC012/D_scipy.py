import sys
from scipy.sparse.csgraph import floyd_warshall
readline = sys.stdin.readline
INF = 10 ** 10

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, readline().rstrip().split())
        path[a-1][b-1] = t
        path[b-1][a-1] = t
    
    G = floyd_warshall(path)    
    res = INF
    for i in range(N):
        res = min(res, max(G[i]))

    print(int(res))

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline
from heapq import heapify, heappush, heappop
MOD = 10 ** 9 + 7
INF = 10 ** 10

def main():
    N = int(readline())
    a, b = map(int, readline().rstrip().split())
    a -= 1
    b -= 1
    M = int(readline())
    path = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, readline().rstrip().split())
        path[x-1].append((1, y-1))  # (距離, 終点)
        path[y-1].append((1, x-1))  # (距離, 終点)
    
    cnt = [0] * N  # 始点から各頂点への最短経路数
    cnt[a] = 1  # 始点aからaへの最短経路数は1
    visited = [False] * N
    que = [(0, a)]
    heapify(que)  # 始点aから各頂点への(距離, 頂点ID)
    dist = [-1] * N  # 始点aから各頂点への距離
    dist[a] = 0  # 始点aからaへの距離は0
    while que:
        d, v = heappop(que)  # 始点から最短距離の頂点を(確定ノード)を取り出す
        visited[v] = True  # 確定フラグを立てる
        # 接続先ノードの情報を更新する
        for d, to in path[v]:
            cost = dist[v] + d
            if cost == dist[to]:
                cnt[to] += cnt[v]
            if dist[to] < 0 or cost < dist[to]:
                dist[to] = cost
                cnt[to] = cnt[v]
                if not visited[to]:
                    heappush(que, (cost, to))

    print(cnt[b] % MOD)

if __name__ == '__main__':
    main()
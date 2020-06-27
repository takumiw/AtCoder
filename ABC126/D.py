import sys
readline = sys.stdin.readline
from heapq import heapify, heappush, heappop

def dijkstra(path, N, start):
    visited = [False] * N
    que = [(0, start)]
    heapify(que)  # 始点aから各頂点への(距離, 頂点ID)
    dist = [-1] * N  # 始点aから各頂点への距離
    dist[start] = 0  # 始点aからaへの距離は0
    while que:
        d, v = heappop(que)  # 始点から最短距離の頂点を(確定ノード)を取り出す
        visited[v] = True  # 確定フラグを立てる
        # 接続先ノードの情報を更新する
        for d, to in path[v]:
            cost = dist[v] + d
            if dist[to] < 0 or cost < dist[to]:
                dist[to] = cost
                if not visited[to]:
                    heappush(que, (cost, to))

    return dist

def main():
    N = int(readline())
    path = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, readline().rstrip().split())
        path[u-1].append((w, v-1))
        path[v-1].append((w, u-1))
    
    dist = dijkstra(path, N, 0)
    for d in dist:
        if d % 2 == 0:
            print(0)
        else:
            print(1)

if __name__ == '__main__':
    main()
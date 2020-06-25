import sys
readline = sys.stdin.readline
from heapq import heapify, heappush, heappop


def dijkstra(path, N, start):
    """
    Args:
        path (list): [[(cost, node), (cost, node), ...], [], [], ...]
    """
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
        a, b, c = map(int, readline().rstrip().split())
        path[a-1].append((c, b-1))
        path[b-1].append((c, a-1))
    
    Q, K = map(int, readline().rstrip().split())
    dist = dijkstra(path, N, K-1)

    for _ in range(Q):
        x, y = map(int, readline().rstrip().split())
        print(dist[x-1] + dist[y-1])


if __name__ == '__main__':
    main()
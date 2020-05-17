import sys
readline = sys.stdin.readline
from heapq import heapify, heappush, heappop

def dijkstra(path, N, start):
    visited = [False] * N
    mark = [-1] * N  # その頂点の次にどの頂点に行くか決定済みのもの
    que = [(0, start, -1)]  # (コスト、頂点、前の頂点)
    heapify(que)  # 始点aから各頂点への(距離, 頂点ID)
    dist = [-1] * N  # 始点aから各頂点への距離
    dist[start] = 0  # 始点aからaへの距離は0
    while que:
        d, v, pre = heappop(que)  # 始点から最短距離の頂点を(確定ノード)を取り出す
        visited[v] = True  # 確定フラグを立てる
        if v > 0:
            if mark[v] != -1 and mark[v] != pre:
                return 'No'
            mark[v] = pre
        # 接続先ノードの情報を更新する
        for d, to in path[v]:
            cost = dist[v] + d
            if dist[to] < 0 or cost < dist[to]:
                dist[to] = cost
                if not visited[to]:
                    heappush(que, (cost, to, v))

    return mark

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, readline().rstrip().split())
        path[a-1].append((1, b-1))
        path[b-1].append((1, a-1))
    
    start = 0
    mark = dijkstra(path, N, start)
    if mark == 'No':
        print('No')
        return

    print('Yes')
    for v in range(1, N):
        print(mark[v] + 1)

if __name__ == '__main__':
    main()
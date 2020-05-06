import sys
readline = sys.stdin.readline
from heapq import heapify, heappush, heappop
INF = 10 ** 9 * 3
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dijkstra(path, N, a):
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
            if dist[to] < 0 or cost < dist[to]:
                dist[to] = cost
                if not visited[to]:
                    heappush(que, (cost, to))

    return dist


def main():
    H, W, T = map(int, readline().rstrip().split())
    HW = H * W
    x = 0
    inp = [readline().rstrip() for _ in range(H)]
    for h in range(H):
        l = inp[h]
        for w in range(W):
            if inp[h][w] == 'S':
                start = h*W + w
            elif inp[h][w] == 'G':
                goal = h*W + w

    mi = 1
    ma = T
    x = T // 2
    while 1:
        path = [[] for _ in range(HW)]
        for h in range(H):
            l = inp[h]
            for w in range(W):
                if inp[h][w] == '#':
                    for dh, dw in directions:
                        if 0 <= h+dh < H and 0 <= w+dw < W:
                            path[(h+dh)*W+(w+dw)].append((x, h*W+w))
                elif inp[h][w] == '.' or inp[h][w] == 'S' or inp[h][w] == 'G':
                    for dh, dw in directions:
                        if 0 <= h+dh < H and 0 <= w+dw < W:
                            path[(h+dh)*W+(w+dw)].append((1, h*W+w))
        
        G = dijkstra(path, HW, start)
        if G[goal] <= T:
            if mi == ma:
                ans = x
                break
            if mi + 1 == ma:
                mi = ma
                x = mi
            else:
                mi = x
                x = (mi + ma) // 2
        else:
            if mi == ma:
                ans = x - 1
                break
            if mi + 1 == ma:
                ma = mi
                x = mi
            else:
                ma = x
                x = (mi + ma) // 2
    
    print(ans)


if __name__ == '__main__':
    main()
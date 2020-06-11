import sys
readline = sys.stdin.readline
from collections import deque
INF = 10 ** 10
directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0)]

def main():
    N, X, Y = map(int, readline().rstrip().split())
    H = W = 403
    mat = [['.'] * W for _ in range(H)]
    for _ in range(N):
        x, y = map(int, readline().rstrip().split())
        mat[y+201][x+201] = '#'

    now = (201, 201)
    goal = (Y+201, X+201)
    dist = [[INF] * W for _ in range(H)]
    dist[now[0]][now[1]] = 0
    que = deque([now])
    while que:
        h, w = que.popleft()
        for dh, dw in directions:
            if not (0 <= h+dh < H and 0 <= w+dw < W):
                continue
            if mat[h+dh][w+dw] == '#':
                continue
            if dist[h+dh][w+dw] > dist[h][w] + 1:
                dist[h+dh][w+dw] = dist[h][w] + 1
                que.append((h+dh, w+dw))

    if dist[goal[0]][goal[1]] == INF:
        print(-1)
    else:
        print(dist[goal[0]][goal[1]])

if __name__ == '__main__':
    main()
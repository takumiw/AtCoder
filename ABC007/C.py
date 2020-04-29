import sys
readline = sys.stdin.readline
from collections import deque
INF = 10 ** 4
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def main():
    H, W = map(int, readline().rstrip().split())
    hs, ws = map(int, readline().rstrip().split())
    hg, wg = map(int, readline().rstrip().split())
    hs, ws, hg, wg = hs-1, ws-1, hg-1, wg-1
    wall = list(readline().rstrip() for _ in range(H))
    maze = [[INF] * W for _ in range(H)]
    maze[hs][ws] = 0

    que = deque([(hs, ws)])
    while que:
        h, w = que.popleft()
        for dh, dw in DIR:
            if 0 <= h+dh < H and 0 <= w+dw < W:
                if wall[h+dh][w+dw] == '#':
                    continue
                if maze[h+dh][w+dw] > maze[h][w] + 1:
                    maze[h+dh][w+dw] = maze[h][w] + 1
                    if h+dh == hg and w+dw == wg:
                        break
                    que.append((h+dh, w+dw))

    print(maze[hg][wg])


if __name__ == '__main__':
    main()
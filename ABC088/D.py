import sys
readline = sys.stdin.readline
from collections import deque
INF = 10 ** 4
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def main():
    H, W = map(int, readline().rstrip().split())
    mat = [readline().rstrip() for _ in range(H)]
    maze = [[INF] * W for _ in range(H)]
    maze[0][0] = 0
    que = deque([(0, 0)])
    flg = True
    while que and flg:
        h, w = que.popleft()
        for dh, dw in directions:
            if 0 <= h+dh < H and 0 <= w+dw < W:
                if mat[h+dh][w+dw] == '.' and maze[h+dh][w+dw] > maze[h][w] + 1:
                    maze[h+dh][w+dw] = maze[h][w] + 1
                    que.append((h+dh, w+dw))
                if h+dh == H-1 and w+dw == W-1:
                    flg = False

    if maze[H-1][W-1] == INF:
        print(-1)
    else:
        cnt_b = sum([l.count('#') for l in mat])
        print(H * W - cnt_b - (maze[H-1][W-1] + 1))

if __name__ == '__main__':
    main()
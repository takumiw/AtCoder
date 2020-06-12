import sys
readline = sys.stdin.readline
from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def main():
    H, W = map(int, readline().rstrip().split())
    mat = [list(readline().rstrip()) for _ in range(H)]

    start = []
    for h in range(H):
        for w in range(W):
            if mat[h][w] == '#':
                start.append((h, w))
    
    res = 0
    que = deque(start)
    while que:
        next_que = deque()
        for h, w in que:
            for dh, dw in directions:
                if not (0 <= h+dh < H and 0 <= w+dw < W):
                    continue
                if mat[h+dh][w+dw] == '#':
                    continue
                mat[h+dh][w+dw] = '#'
                next_que.append((h+dh, w+dw))

        res += 1
        que = next_que

    print(res - 1)


if __name__ == '__main__':
    main()
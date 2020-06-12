import sys
readline = sys.stdin.readline
from collections import deque
INF = 10 ** 7
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def main():
    H, W, N = map(int, readline().rstrip().split())
    mat = [readline().rstrip() for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if mat[h][w] == 'S':
                hs, ws = h, w
                break
        else:
            continue
        break
    
    res = 0
    for n in range(1, N+1):
        n = str(n)
        dist = [[INF] * W for _ in range(H)]
        dist[hs][ws] = 0
        que = deque([(hs, ws)])
        flg = True

        while que and flg:
            h, w = que.popleft()
            for dh, dw in directions:
                if not (0 <= h+dh < H and 0 <= w+dw < W):
                    continue
                if mat[h+dh][w+dw] == 'X':
                    continue
                if mat[h+dh][w+dw] == n:
                    res += dist[h][w] + 1
                    hs, ws = h + dh, w + dw
                    flg = False
                    break
                else:
                    if dist[h+dh][w+dw] > dist[h][w] + 1:
                        dist[h+dh][w+dw] = dist[h][w] + 1
                        que.append((h+dh, w+dw))
    
    print(res)


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline
from scipy.sparse.csgraph import dijkstra
INF = 10 ** 9 * 3
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


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
        path = [[INF] * HW for _ in range(HW)]
        for h in range(H):
            l = inp[h]
            for w in range(W):
                if inp[h][w] == '#':
                    for dh, dw in directions:
                        if 0 <= h+dh < H and 0 <= w+dw < W:
                            path[(h+dh)*W+(w+dw)][h*W+w] = x
                elif inp[h][w] == '.' or inp[h][w] == 'S' or inp[h][w] == 'G':
                    for dh, dw in directions:
                        if 0 <= h+dh < H and 0 <= w+dw < W:
                            path[(h+dh)*W+(w+dw)][h*W+w] = 1
        
        G = dijkstra(path, indices=start)
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
import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

H, W = map(int, readline().rstrip().split())
mat = [list(readline().rstrip()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]

def dfs(h, w):
    if visited[h][w]:
        return
    visited[h][w] = True
    if mat[h][w] == 'g':
        print('Yes')
        exit()
    for dh, dw in directions:
        if not (0 <= h + dh < H and 0 <= w + dw < W):
            continue
        if visited[h+dh][w+dw] or mat[h+dh][w+dw] == '#':
            continue
        dfs(h+dh, w+dw)
    return


def main():
    for h in range(H):
        for w in range(W):
            if mat[h][w] == 's':
                start = (h, w)
                break
            else:
                continue
            break

    dfs(*start)
    print('No')


if __name__ == '__main__':
    main()
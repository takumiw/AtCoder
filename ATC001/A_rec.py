import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
matrix = [list(input()) for _ in range(H)]


def dfs(h, w):
    if h < 0 or w < 0 or h >= H or w >= W:
        return
    if matrix[h][w] == '#':
        return
    if matrix[h][w] == 'g':
        print('Yes')
        exit()
    matrix[h][w] = '#'
    dfs(h+1, w)
    dfs(h-1, w)
    dfs(h, w+1)
    dfs(h, w-1)
    return


def solve():
    for h in range(H):
        for w in range(W):
            if matrix[h][w] == 's':
                s = (h, w)  # スタート地点の座標
                break
    dfs(s[0], s[1])
    print('No')


if __name__ == '__main__':
    solve()
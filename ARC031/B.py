import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

H = W = 10
mat = [list(readline().rstrip()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]

def match(mat, visited):
    for h in range(H):
        for w in range(W):
            if mat[h][w] == 'o':
                if not visited[h][w]:
                    return False
    return True

def dfs(h, w):
    visited[h][w] = True
    for dh, dw in directions:
        if not (0 <= h + dh < H and 0 <= w + dw < W):
            continue
        if mat[h+dh][w+dw] != 'o':
            continue
        if visited[h+dh][w+dw]:
            continue
        dfs(h+dh, w+dw)
    return
    
def main():
    global visited
    for h in range(H):
        for w in range(W):
            if mat[h][w] == 'o':
                continue
            mat[h][w] = 'o'
            visited = [[False] * W for _ in range(H)]
            dfs(h, w)
            if match(mat, visited):
                print('YES')
                return
            mat[h][w] = 'x'

    print('NO')

if __name__ == '__main__':
    main()
from collections import deque

H, W = map(int, input().split())
inf = H * W + 1

def solve():
    matrix = [[-1 for _ in range(W+2)]] + [[-1] + list(input()) + [-1] for _ in range(H)] + [[-1 for _ in range(W+2)]]
    for i, l in enumerate(matrix[1:-1]):
        for j, v in enumerate(l[1:-1]):
            if v == 's':
                s = (i+1, j+1)  # スタート地点の座標
                matrix[i+1][j+1] = 0
            elif v == 'g':
                g = (i+1, j+1)  # ゴール地点の座標
                matrix[i+1][j+1] = inf
            elif v == '#':
                matrix[i+1][j+1] = -1  # 塀
            else:
                matrix[i+1][j+1] = inf  # 道

    queue = deque()
    queue.append(s)
    while queue:
        h, w = queue.popleft()
        if (h, w) == g:
            print('Yes')
            exit()
        for dh, dw in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if matrix[h+dh][w+dw] > matrix[h][w]:
                matrix[h+dh][w+dw] = matrix[h][w] + 1
                queue.append((h+dh, w+dw))

    print('No')

if __name__ == '__main__':
    solve()
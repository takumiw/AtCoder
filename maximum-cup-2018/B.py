import sys
readline = sys.stdin.readline
from collections import deque
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

def main():
    A,  B = map(int, readline().rstrip().split())
    H, W = map(int, readline().rstrip().split())
    mat = [readline().rstrip() for _ in range(H)]
    hg, wg = H - 2, W - 2
    que = deque([(1, 1, 2, A, B)])  # (h, w, 向き, a, b) 向き 0-4: 北東南西
    visited = [[[[[False] * 4 for _ in range(W)] for _ in range(H)] for _ in range(B + 1)] for _ in range(A + 1)]  # visited[a][b][h][w][d]
    while que:
        h, w, d, a, b = que.popleft()
        if visited[a][b][h][w][d]:
            continue
        visited[a][b][h][w][d] = True
        if h == hg and w == wg and a == b == 0:
            print('Yes')
            return
        
        # 向きを変えずに一マス前進
        dh, dw = directions[d]
        if mat[h+dh][w+dw] == '.':
            que.append((h+dh, w+dw, d, a, b))
        
        # 右に90度向きを変えてから一マス前進
        if b > 0:
            next_d = (d + 1) % 4
            dh, dw = directions[next_d]
            if mat[h+dh][w+dw] == '.':
                que.append((h+dh, w+dw, next_d, a, b-1))
        
        # 左に90度向きを変えてから一マス前進
        if a > 0:
            next_d = (d - 1) % 4
            dh, dw = directions[next_d]
            if mat[h+dh][w+dw] == '.':
                que.append((h+dh, w+dw, next_d, a-1, b))
    
    print('No')

if __name__ == '__main__':
    main()
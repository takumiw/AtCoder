import sys
sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

class Ans():

    def __init__(self, H, W, mat):
        self.H = H
        self.W = W
        self.mat = mat
        self.visited = [[False] * W for _ in range(H)]

    def dfs(self, h, w):
        if self.mat[h][w] == 0 or self.visited[h][w] == True:
            return
        
        self.visited[h][w] = True
        for dh, dw in directions:
            if not (0 <= h + dh < self.H and 0 <= w + dw < self.W):
                continue
            if self.mat[h+dh][w+dw] == 0 or self.visited[h+dh][w+dw] == True:
                continue
            self.dfs(h+dh, w+dw)
        return

def main():
    while 1:
        W, H = map(int, readline().rstrip().split())
        if W == H == 0:
            break

        mat = [list(map(int, readline().rstrip().split())) for _ in range(H)]
        ans = Ans(H, W, mat)

        res = 0
        for h in range(H):
            for w in range(W):
                if ans.mat[h][w] == 1 and ans.visited[h][w] == False:
                    res += 1
                ans.dfs(h, w)

        print(res)

if __name__ == '__main__':
    main()
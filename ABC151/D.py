from collections import deque

def main():
    H, W = map(int, input().split())
    maze = [list(input()) for _ in range(H)]
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    ans = 0
    for h in range(H):
        for w in range(W):
            if maze[h][w] == '#':
                continue

            goal_dists = [[-1] * W for _ in range(H)]
            goal_dists[h][w] = 0
            d = deque([[h, w]])

            while d:
                ht, wt = d.popleft()
                for dh, dw in directions:
                    if not (0 <= ht+dh < H and 0 <= wt+dw < W):
                        continue
                    if maze[ht+dh][wt+dw] == '#':
                        continue
                    if goal_dists[ht+dh][wt+dw] == -1:
                        goal_dists[ht+dh][wt+dw] = goal_dists[ht][wt] + 1
                        d.append([ht+dh, wt+dw])
            
            ans = max(ans, max([max(l) for l in goal_dists]))

    print(ans)

if __name__ == "__main__":
    main()
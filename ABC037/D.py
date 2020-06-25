import sys
sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline
MOD = 10 ** 9 + 7
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

H, W = map(int, readline().rstrip().split())
mat = [list(map(int, readline().rstrip().split())) for _ in range(H)]
cnt = [[-1] * W for _ in range(H)]


def dfs(h, w):
    if cnt[h][w] != -1:
        return
    cnt[h][w] = 1
    for dh, dw in direction:
        if not (0 <= h+dh < H and 0 <= w+dw < W):
            continue
        if mat[h+dh][w+dw] > mat[h][w]:
            dfs(h+dh, w+dw)
            cnt[h][w] += cnt[h+dh][w+dw] % MOD


def main():
    for h in range(H):
        for w in range(W):
            dfs(h, w)

    print(sum([sum(cnt[i]) for i in range(H)]) % MOD)


if __name__ == '__main__':
    main()
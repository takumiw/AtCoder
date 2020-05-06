import sys
readline = sys.stdin.readline

def main():
    H, W, K = map(int, readline().rstrip().split())
    mat = [readline().rstrip() for _ in range(H)]
    wht_up = [[0] * W for _ in range(H)]
    wht_up[0] = [1 if mat[0][w]=='o' else 0 for w in range(W)]
    wht_down = [[0] * W for _ in range(H)]
    wht_down[-1] = [1 if mat[-1][w]=='o' else 0 for w in range(W)]

    for h in range(1, H):
        for w in range(W):
            if mat[h][w] == 'o':
                wht_up[h][w] = wht_up[h-1][w] + 1

            if mat[H-1-h][w] == 'o':
                wht_down[H-1-h][w] = wht_down[H-h][w] + 1

    ans = 0
    for h in range(K-1, H-K+1):
        wht_up_h = wht_up[h]
        wht_down_h = wht_down[h]
        for w in range(K-1, W-K+1):
            flg = True
            for dw in range(-K+1, K):
                if wht_up_h[w+dw] < K-abs(dw) or wht_down_h[w+dw] < K-abs(dw):
                    flg = False
                    break
                else:
                    continue
                break
            if flg:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
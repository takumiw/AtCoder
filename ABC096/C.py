import sys
readline = sys.stdin.readline
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def main():
    H, W = map(int, readline().rstrip().split())
    S = [readline().rstrip() for _ in range(H)]
    res = 'Yes'
    for h in range(H):
        for w in range(W):
            if S[h][w] != '#':
                continue
            flg = False
            for dh, dw in directions:
                if 0 <= h+dh < H and 0 <= w+dw < W:
                    if S[h+dh][w+dw] == '#':
                        flg = True
                        break
            if not flg:
                res = 'No'
                break
        else:
            continue
        break

    print(res)

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    H, W = map(int, readline().rstrip().split())
    mat = [list(readline().rstrip()) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if mat[h][w] == '.':
                cnt = 0
                for dh in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if 0 <= h+dh < H and 0 <= w+dw < W:
                            if mat[h+dh][w+dw] == '#':
                                cnt += 1
                mat[h][w] = cnt
    
    for l in mat:
        print(*l, sep='')

if __name__ == '__main__':
    main()
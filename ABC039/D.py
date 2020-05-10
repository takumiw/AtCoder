import sys
readline = sys.stdin.readline
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def main():
    H, W = map(int, readline().rstrip().split())
    mat = [list(readline().rstrip()) for _ in range(H)]
    mat2 = [l[:] for l in mat]
    res = [['.'] * W for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if mat[h][w] != '#':
                continue
            flg = True
            for dh, dw in directions:
                if 0 <= h+dh < H and 0 <= w+dw < W:
                    if mat[h+dh][w+dw] != '#':
                        flg = False
                        break
            
            if flg:
                for dh, dw in directions:
                    if 0 <= h+dh < H and 0 <= w+dw < W:
                        mat2[h+dh][w+dw] = '.'
                mat2[h][w] = '.'
                res[h][w] = '#'
    
    if sum(['#' in l for l in mat2]):
        print('impossible')
    else:
        print('possible')
        for l in res:
            print(*l, sep='')

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    H, W = map(int, readline().rstrip().split())
    A = [list(map(int, readline().rstrip().split())) for _ in range(H)]
    res = []
    cnt = 0
    for h in range(H):
        for w in range(W-1):
            if A[h][w] % 2 == 1:
                A[h][w+1] += 1
                cnt += 1
                res.append('{} {} {} {}'.format(h+1, w+1, h+1, w+2))

    for h in range(H-1):
        if A[h][W-1] % 2 == 1:
            A[h+1][W-1] += 1
            cnt += 1
            res.append('{} {} {} {}'.format(h+1, W, h+2, W))
    
    print(cnt)
    print(*res, sep='\n')


if __name__ == '__main__':
    main()
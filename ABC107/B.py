import sys
readline = sys.stdin.readline

def main():
    H, W = map(int, readline().rstrip().split())
    mat = []
    for _ in range(H):
        inp = readline().rstrip()
        if '#' not in inp:
            continue
        mat.append(list(inp))
    
    ws = []
    for w in range(W):
        flg = False
        for h in range(len(mat)):
            if mat[h][w] == '#':
                flg = True
                break
        if flg:
            ws.append(w)
    
    ans = [''.join([l[j] for j in range(len(l)) if j in ws]) for l in mat]
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
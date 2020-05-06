import sys
readline = sys.stdin.readline

def main():
    H, W, K = map(int, readline().rstrip().split())
    mat = [readline().rstrip() for _ in range(H)]
    ans = 0
    for h in range(K-1, H-K+1):
        for w in range(K-1, W-K+1):
            flg = True
            for dh in range(-K+1, K):
                for wi in range(w-K+1+abs(dh), w+K-abs(dh)):
                    if mat[h+dh][wi] == 'x':
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
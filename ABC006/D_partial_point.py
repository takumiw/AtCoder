import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    C = [int(readline()) for _ in range(N)]
    ans = N
    for i in range(1, 2**N):
        b = bin(i)[2:].zfill(N)
        left = [C[i] for i, e in enumerate(b) if e == '1']
        flg = True
        v = left[0]
        for l in left[1:]:
            if l < v:
                flg = False
                break
            v = l
        if flg:
            ans = min(ans, N-len(left))

    print(ans)

if __name__ == '__main__':
    main()
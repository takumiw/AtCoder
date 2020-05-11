import sys
readline = sys.stdin.readline

def main():
    N, M, X = map(int, readline().rstrip().split())
    C, A = [], []
    for _ in range(N):
        c, *a = map(int, readline().rstrip().split())
        C.append(c)
        A.append(a)
    res = 10 ** 10
    for i in range(2**N):
        b = bin(i)[2:].zfill(N)
        buy_idx = [i for i, e in enumerate(b) if e == '1']
        flg = True
        for alg in range(M):
            if sum([A[j][alg] for j in buy_idx]) < X:
                flg = False
                break
        if flg:
            res = min(res, sum([C[j] for j in buy_idx]))

    if res == 10 ** 10:
        print(-1)
    else:
        print(res)

if __name__ == '__main__':
    main()
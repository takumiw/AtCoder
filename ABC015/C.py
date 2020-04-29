import sys
readline = sys.stdin.readline
from itertools import permutations

def base_10_to_n(i, n):
    if i//n:
        return base_10_to_n(i//n, n) + str(i % n)
    return str(i % n)

def main():
    N, K = map(int, readline().rstrip().split())
    T = [list(map(int, readline().rstrip().split())) for _ in range(N)]
    l = [i for i in range(K)]
    idx = [base_10_to_n(i, K).zfill(N) for i in range(K**N)]
    for ix in idx:
        ix = list(map(int, list(ix)))
        q = T[0][ix[0]]
        for i, x in enumerate((ix[1:])):
            q ^= T[i+1][x]
        if q == 0:
            print('Found')
            return

    print('Nothing')
    return


if __name__ == '__main__':
    main()
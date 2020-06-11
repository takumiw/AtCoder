import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    Q = int(readline())
    H = [i for i in range(N)]
    W = [i for i in range(N)]
    is_trans = False
    for _ in range(Q):
        q, *ab = map(int, readline().rstrip().split())
        if q == 1:
            a, b = ab
            if not is_trans:
                next_a = H[b-1]
                next_b = H[a-1]
                H[a-1] = next_a
                H[b-1] = next_b
            else:
                next_a = W[b-1]
                next_b = W[a-1]
                W[a-1] = next_a
                W[b-1] = next_b
        elif q == 2:
            a, b = ab
            if not is_trans:
                next_a = W[b-1]
                next_b = W[a-1]
                W[a-1] = next_a
                W[b-1] = next_b
            else:
                next_a = H[b-1]
                next_b = H[a-1]
                H[a-1] = next_a
                H[b-1] = next_b
        elif q == 3:
            is_trans ^= True
        else:
            a, b = ab
            if not is_trans:
                i = H[a-1] + 1
                j = W[b-1] + 1
                print(N * (i-1) + j - 1)
            else:
                i = W[a-1] + 1
                j = H[b-1] + 1
                print(N * (j-1) + i - 1)

if __name__ == '__main__':
    main()
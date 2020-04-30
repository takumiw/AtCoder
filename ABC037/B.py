import sys
readline = sys.stdin.readline

def main():
    N, Q = map(int, readline().rstrip().split())
    A = [0] * N
    for _ in range(Q):
        l, r, t = map(int, readline().rstrip().split())
        for i in range(l-1, r):
            A[i] = t

    print(*A, sep='\n')

if __name__ == '__main__':
    main()
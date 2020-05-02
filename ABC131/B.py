import sys
readline = sys.stdin.readline

def main():
    N, L = map(int, readline().rstrip().split())
    A = [L+i-1 for i in range(1, N+1)]
    A_abs = [abs(a) for a in A]
    mi_idx = A_abs.index(min(A_abs))
    print(sum(A) - A[mi_idx])

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    X, Y, Z, K = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    B = list(map(int, readline().rstrip().split()))
    C = list(map(int, readline().rstrip().split()))

    ab = [a + b for a in A for b in B]
    ab = sorted(ab, reverse=True)[:K]

    abc = [v + c for v in ab for c in C]
    print(*sorted(abc, reverse=True)[:K], sep='\n')


if __name__ == '__main__':
    main()
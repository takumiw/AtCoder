import sys
sys.setrecursionlimit(10 ** 6)

def main():
    N, A, B = map(int, sys.stdin.readline().rstrip().split())
    print(min(B, A*N))


if __name__ == '__main__':
    main()
import sys
sys.setrecursionlimit(10 ** 6)

def main():
    N, M, X, Y = map(int, sys.stdin.readline().rstrip().split())
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    x = max(X, max(x))
    y = list(map(int, sys.stdin.readline().rstrip().split()))
    y = min(Y, min(y))
    if x < y:
        print('No War')
    else:
        print('War')


if __name__ == '__main__':
    main()
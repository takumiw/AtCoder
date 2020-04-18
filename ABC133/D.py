import sys
sys.setrecursionlimit(10 ** 6)

def main():
    N = int(input())
    A = list(map(int, sys.stdin.readline().rstrip().split()))

    x1 = sum([a if i % 2 == 0 else -a for i, a in enumerate((A))])
    X = [x1]
    for i in range(1, N):
        xi = 2 * A[i-1] - X[i-1]
        X.append(xi)
    
    print(*X)


if __name__ == '__main__':
    main()
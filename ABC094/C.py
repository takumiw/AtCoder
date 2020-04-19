import sys

def main():
    N = int(sys.stdin.readline())
    X = list(map(int, sys.stdin.readline().rstrip().split()))
    
    x_asc = sorted(X)
    m1, m2 = x_asc[N//2-1], x_asc[N//2]
    for x in X:
        if x <= m1:
            print(m2)
        else:
            print(m1)


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    X = list(map(int, readline().rstrip().split()))

    if N >= M:
        print(0)
        return

    X.sort()
    X = [abs(X[i+1]-X[i]) for i in range(M-1)]
    X.sort(reverse=True)
    print(sum(X[N-1:]))


if __name__ == '__main__':
    main()
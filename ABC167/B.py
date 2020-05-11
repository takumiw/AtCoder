import sys
readline = sys.stdin.readline

def main():
    A, B, C, K = map(int, readline().rstrip().split())
    if A >= K:
        print(K)
    elif A + B >= K:
        print(A)
    else:
        print(A - (K - A - B))


if __name__ == '__main__':
    main()
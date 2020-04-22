import sys
readline = sys.stdin.readline

def main():
    N, T = map(int, readline().rstrip().split())
    t = list(map(int, readline().rstrip().split()))
    d = [t[i] - t[i-1] for i in range(1, N)]
    print(sum([min(T, e) for e in d]) + T)


if __name__ == '__main__':
    main()
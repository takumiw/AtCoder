import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    m = [a//400 for a in A if a < 3200]

    mi = len(set(m))
    ma = len(set(m)) + (N - len(m))
    print(max(1, mi), ma)    


if __name__ == '__main__':
    main()
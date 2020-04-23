import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    print(((N-M)*100 + M*1900) * 2**M)


if __name__ == '__main__':
    main()
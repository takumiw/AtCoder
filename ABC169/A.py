import sys
readline = sys.stdin.readline

def main():
    A, B = map(int, readline().rstrip().split())
    print(A * B)


if __name__ == '__main__':
    main()
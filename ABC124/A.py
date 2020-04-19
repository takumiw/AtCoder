import sys
readline = sys.stdin.readline

def main():
    A, B = map(int, readline().rstrip().split())
    print(max(A, B) + max(max(A, B) - 1, min(A, B)))


if __name__ == '__main__':
    main()
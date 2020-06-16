import sys
readline = sys.stdin.readline


def main():
    X, Y = map(int, readline().rstrip().split())
    for i in range(X + 1):
        j = X - i
        if 2 * i + 4 * j == Y or 2 * j + 4 * i == Y:
            print('Yes')
            return
    
    print('No')


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline


def main():
    a = int(readline())
    print(a + a ** 2 + a ** 3)


if __name__ == '__main__':
    main()
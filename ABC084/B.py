import sys
readline = sys.stdin.readline


def main():
    A, B = map(int, readline().rstrip().split())
    S = readline().rstrip()
    if S[:A].isdecimal() and S[A] == '-' and  S[A+1:].isdecimal():
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
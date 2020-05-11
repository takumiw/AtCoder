import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip()
    T = readline().rstrip()
    if S == T[:-1]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
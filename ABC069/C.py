import sys
readline = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, readline().rstrip().split()))
    m2 = len([a for a in A if a % 2 == 0])
    m4 = len([a for a in A if a % 4 == 0])
    mx = N - m2
    if mx == m4 + 1 and m2 - m4 == 0:
        print('Yes')
    elif mx > m4:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
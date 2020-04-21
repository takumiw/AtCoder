import sys
readline = sys.stdin.readline

def main():
    N = int(input())
    L = list(map(int, readline().rstrip().split()))
    if max(L) < sum(L) - max(L):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
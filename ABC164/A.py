import sys
readline = sys.stdin.readline

def main():
    S, W = map(int, readline().rstrip().split())
    if W >= S:
        print('unsafe')
    else:
        print('safe')


if __name__ == '__main__':
    main()
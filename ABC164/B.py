import sys
readline = sys.stdin.readline

def main():
    A, B, C, D = map(int, readline().rstrip().split())
    for i in range(1000):
        if C <= B:
            print('Yes')
            return
        C -= B
        if A <= D:
            print('No')
            return
        A -= D


if __name__ == '__main__':
    main()
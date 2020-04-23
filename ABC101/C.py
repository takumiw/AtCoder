import sys
readline = sys.stdin.readline
import math

def main():
    N, K = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    print(math.ceil((N-1)/(K-1)))


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline
import math

def main():
    N, M = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    print(max(N-sum(A), -1))


if __name__ == '__main__':
    main()
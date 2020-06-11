import sys
readline = sys.stdin.readline
import math

def main():
    A, R, N = map(int, readline().rstrip().split())
    if R == 1:
        print(A)
    elif N - 1 > math.log(10**9/A, R):
        print('large')
    else:
        res = A * R ** (N - 1)
        print(res)

if __name__ == '__main__':
    main()
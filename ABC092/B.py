import sys
readline = sys.stdin.readline
import math

def main():
    N = int(readline())
    D, X = map(int, readline().rstrip().split())
    for _ in range(N):
        a = int(readline())
        X += math.floor((D-1) / a + 1)

    print(X)


if __name__ == '__main__':
    main()
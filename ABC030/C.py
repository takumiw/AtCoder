import sys
readline = sys.stdin.readline
from bisect import bisect_left

def main():
    N, M = map(int, readline().rstrip().split())
    X, Y = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    B = list(map(int, readline().rstrip().split()))
    ans = 0
    time = 0
    while True:
        i = bisect_left(A, time)
        if i < N:
            ans += 1
            time = A[i] + X
        else:
            break
        i = bisect_left(B, time)
        if i < M:
            ans += 1
            time = B[i] + Y
        else:
            break

    print(ans // 2)


if __name__ == '__main__':
    main()
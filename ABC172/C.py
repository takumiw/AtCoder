import sys
readline = sys.stdin.readline
from bisect import bisect_right

def main():
    N, M, K = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    B = list(map(int, readline().rstrip().split()))

    a_acc, b_acc = A[:], B[:]
    for i in range(1, N):
        a_acc[i] += a_acc[i-1]
    
    for i in range(1, M):
        b_acc[i] += b_acc[i-1]
    
    res = 0
    for i, a in enumerate(a_acc):
        if a > K:
            break
        left = K - a
        j = bisect_right(b_acc, left)
        res = max(res, i + 1 + j)
    
    res = max(res, bisect_right(b_acc, K))  # Aを1冊も読まない場合
    print(res)

if __name__ == '__main__':
    main()
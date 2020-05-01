import sys
readline = sys.stdin.readline
from bisect import bisect_left

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    A.sort()
    B = list(map(int, readline().rstrip().split()))
    B.sort()
    C = list(map(int, readline().rstrip().split()))
    C.sort()

    B2 = [bisect_left(A, b) for b in B]
    B3 = [B2[0]]
    pre = B3[0]
    for b in B2[1:]:
        pre += b
        B3.append(pre)
    C2 = [bisect_left(B, c) for c in C]
    B3.append(0)
    ans = sum([B3[c-1] for c in C2])
    print(ans)

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    for i in range(1, N):
        A[i] += A[i-1]
    cnt1, cnt2 = 0, 0
    ref1, ref2 = 0, 0
    for i, a in enumerate(A):
        if i % 2 == 0:
            if a <= ref1:
                cnt1 += ref1 - a + 1
                ref1 -= ref1 - a + 1
            if a >= ref2:
                cnt2 += a - ref2 + 1
                ref2 += a - ref2 + 1
        if i % 2 == 1:
            if a >= ref1:
                cnt1 += a - ref1 + 1
                ref1 += a - ref1 + 1
            if a <= ref2:
                cnt2 += ref2 - a + 1
                ref2 -= ref2 - a + 1

    print(min(cnt1, cnt2))

if __name__ == '__main__':
    main()
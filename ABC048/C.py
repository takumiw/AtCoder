import sys
readline = sys.stdin.readline

def main():
    N, x = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    ans = 0
    for i, a in enumerate(A):
        if a > x:
            ans += a - x
            A[i] = x
    
    pre = 0
    for i, a in enumerate(A):
        if pre + a > x:
            A[i] = x - pre
            ans += a - A[i]
        pre = A[i]
    
    print(ans)

if __name__ == '__main__':
    main()
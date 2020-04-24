import sys
readline = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, readline().rstrip().split()))
    x = 0
    y = sum(A)
    ans = 10 ** 10
    for i in range(N-1):
        x += A[i]
        y -= A[i]
        ans = min(ans, abs(x-y))
    
    print(ans)


if __name__ == '__main__':
    main()
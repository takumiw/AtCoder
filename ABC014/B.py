import sys
readline = sys.stdin.readline

def main():
    n, X = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    b = bin(X)[2:].zfill(n)
    ans = 0
    for i, v in enumerate(b[::-1]):
        if v == '1':
            ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()
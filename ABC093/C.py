import sys
readline = sys.stdin.buffer.readline

def main():
    A, B, C = map(int, readline().rstrip().split())

    m = max(A, B, C)
    if m == A:
        ma = max(B, C)
        ans = m - ma
        B += ans
        C += ans
    elif m == B:
        ma = max(C, A)
        ans = m - ma
        C += ans
        A += ans
    else:
        ma = max(A, B)
        ans = m - ma
        A += ans
        B += ans
    
    b = (max(A, B, C) - min(A, B, C)) % 2
    ans += (max(A, B, C) - min(A, B, C)) // 2 + b * 2
    print(ans)


if __name__ == '__main__':
    main()
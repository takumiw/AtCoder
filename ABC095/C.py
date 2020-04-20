import sys
readline = sys.stdin.buffer.readline

def main():
    A, B, C, X, Y = map(int, readline().rstrip().split())
    if A + B <= 2 * C:
        print(X * A + Y * B)
        return
    
    m = min(X, Y)
    ans = m * 2 * C
    X -= m
    Y -= m
    ans += min(X * A + Y * B, max(X, Y) * 2 * C)
    
    print(ans)


if __name__ == '__main__':
    main()
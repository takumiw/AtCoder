import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    for q in range(M//2+1):
        if (M - 2*q) % 3 == 0:
            b = (M - 2*q) // 3
            p = N - b
            c = q - p
            a = p - c
            if 0 <= a <= M and 0 <= c <= M:
                print(a, b, c)
                return
    
    print(-1, -1, -1)

if __name__ == '__main__':
    main()
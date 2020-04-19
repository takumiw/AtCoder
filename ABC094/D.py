import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))

    n = max(A)
    a = -1
    d = n
    for e in A:
        if e == n:
            continue
        if abs(e - n/2) < d:
            a = e
            d = abs(e - n/2)
    
    print(n, a)


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    NG = [int(readline()) for _ in range(3)]
    if N in NG:
        print('NO')
        return
    NG.sort()
    n = N
    cnt = 0
    while n > 0:
        if n-3 not in NG:
            n -= 3
            cnt += 1
            continue
        if n-2 not in NG:
            n -= 2
            cnt += 1
            continue
        if n-1 not in NG:
            n -= 1
            cnt += 1
            continue
        print('NO')
        return

    if cnt <= 100:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline


def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    A.sort()

    M = A[-1]
    flg = [0] * (M + 1)
    res = 0

    for a in A:
        if flg[a] == 0:
            res += 1
        if flg[a] == 2:
            res -= 1
            flg[a] = 1
        if flg[a] > 0:
            continue
        flg[a] = 2
        for i in range(2, 10**6):
            if a * i > M:
                break
            flg[a*i] = 1
    
    print(res)


if __name__ == '__main__':
    main()
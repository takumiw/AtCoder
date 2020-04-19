import sys
readline = sys.stdin.readline

def main():
    N = int(input())
    H = list(map(int, readline().rstrip().split()))
    m = H[0]
    cnt = 1
    for h in H[1:]:
        if h >= m:
            cnt += 1
        m = max(m, h)
    print(cnt)


if __name__ == '__main__':
    main()
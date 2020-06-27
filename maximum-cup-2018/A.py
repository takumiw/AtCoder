import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    res = 0
    for _ in range(N):
        t, d, m = map(int, readline().rstrip().split())
        if d / (t + 10) >= 1:
            res += m

    print(res)

if __name__ == '__main__':
    main()
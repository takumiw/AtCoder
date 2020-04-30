import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    AB = [list(map(int, readline().rstrip().split())) for _ in range(N)]
    CD = [list(map(int, readline().rstrip().split())) for _ in range(M)]
    for a, b in AB:
        dist = 10**10
        ans = -1
        for i, (c, d) in enumerate(CD):
            if abs(a-c) + abs(b-d) < dist:
                dist = abs(a-c) + abs(b-d)
                ans = i + 1
        print(ans)


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    F = []
    for _ in range(N):
        inp = list(map(int, readline().rstrip().split()))
        F.append(set([i for i, e in enumerate(inp) if e]))

    P = [list(map(int, readline().rstrip().split())) for _ in range(N)]
    ans = -10**10
    for i in range(1, 2**10):
        b = bin(i)[2:].zfill(10)
        t = set([j for j, e in enumerate(b) if e == '1'])
        pro = 0
        for f, p in zip(F, P):
            d = f & t
            pro += p[len(d)]
        ans = max(ans, pro)
    
    print(ans)


if __name__ == '__main__':
    main()
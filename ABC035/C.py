import sys
readline = sys.stdin.readline

def main():
    N, Q = map(int, readline().rstrip().split())
    res = [0] * (N+1)
    for _ in range(Q):
        l, r = map(int, readline().rstrip().split())
        res[l-1] += 1
        res[r] -= 1
    
    s = res[0]
    for i in range(1, N):
        s += res[i]
        res[i] = s
    
    res = [r % 2 for r in res[:-1]]
    print(*res, sep='')


if __name__ == '__main__':
    main()
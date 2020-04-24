import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    d = {}
    for _ in range(N):
        a, b = map(int, readline().rstrip().split())
        d.setdefault(a, 0)
        d[a] += b
    
    keys, vals = d.keys(), d.values()
    z = zip(keys, vals)
    z = sorted(z)
    keys, vals = zip(*z)
    s = 0
    for k, v in zip(keys, vals):
        if s + v < K:
            s += v
        else:
            ans = k
            break
    print(ans)


if __name__ == '__main__':
    main()
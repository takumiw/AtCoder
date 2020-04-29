import sys
readline = sys.stdin.readline

def main():
    N, D, K = map(int, readline().rstrip().split())
    lr = [list(map(int, readline().rstrip().split())) for _ in range(D)]
    st = [list(map(int, readline().rstrip().split())) for _ in range(K)]

    for s, t in st:
        mi = s
        ma = s
        for i, (l, r) in enumerate(lr):
            if (mi <= r <= ma) or (mi <= l <= ma) or (l <= mi and r >= ma):
                mi = min(mi, l)
                ma = max(ma, r)
            if mi <= t <= ma:
                print(i+1)
                break
                

if __name__ == '__main__':
    main()
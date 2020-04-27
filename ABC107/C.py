import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    X = list(map(int, readline().rstrip().split()))
    len_m = len([x for x in X if x < 0])
    ans = 10**10
    for i in range(max(0, len_m-K), min(len_m+K, N-K+1)):
        l = X[i]
        r = X[i+K-1]
        if l < 0 and r > 0:
            c = min(abs(l) * 2 + r, abs(l) + r * 2)
        else:
            c = max(abs(l), abs(r))
        ans = min(ans, c)

    print(ans)


if __name__ == '__main__':
    main()
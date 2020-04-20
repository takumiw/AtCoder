import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    S = list(int(readline()) for _ in range(N))

    if 0 in S:
        print(N)
        return
    
    r = 0
    ans = 0
    m = 1
    for l in range(N):
        while r < N and m * S[r] <= K:
            m *= S[r]
            r += 1
        ans = max(ans, r-l)
        m = max(m // S[l], 1)
        r = max(r, l+1)
    
    print(ans)


if __name__ == '__main__':
    main()
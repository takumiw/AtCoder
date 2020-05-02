import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    S = []
    for _ in range(M):
        _, *s = map(int, readline().rstrip().split())
        S.append(set(s))
    P = list(map(int, readline().rstrip().split()))

    ans = 0
    for i in range(2**N):
        b = bin(i)[2:].zfill((N))
        b = set([i+1 for i, e in enumerate(b) if e == '1'])
        flg = True
        for j, s in enumerate(S):
            if len(s&b) % 2 != P[j]:
                flg = False
                break
        if flg:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()
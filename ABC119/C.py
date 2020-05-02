import sys
readline = sys.stdin.readline

def base_10_to_n(i, n):
    if i//n:
        return base_10_to_n(i//n, n) + str(i % n)
    return str(i % n)

def main():
    N, A, B, C = map(int, readline().rstrip().split())
    l = [int(readline()) for _ in range(N)]
    ans = 10**6
    for i in range(4**N):
        b = base_10_to_n(i, 4).zfill(N)
        if '1' not in b or '2' not in b or '3' not in b:
            continue
        ai = [l[j] for j, e in enumerate(b) if e == '1']
        bi = [l[j] for j, e in enumerate(b) if e == '2']
        ci = [l[j] for j, e in enumerate(b) if e == '3']
        cost = (len(ai)+len(bi)+len(ci)-3) * 10 + abs(A-sum(ai)) + abs(B-sum(bi)) + abs(C-sum(ci))
        ans = min(ans, cost)

    print(ans)

if __name__ == '__main__':
    main()
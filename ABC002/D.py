import sys
readline = sys.stdin.readline


def main():
    N, M = map(int, readline().rstrip().split())
    path = [[False] * N for _ in range(N)]
    for _ in range(M):
        x, y = map(int, readline().rstrip().split())
        path[x-1][y-1] = True
        path[y-1][x-1] = True
    
    res = 1
    for i in range(1, 2**N):
        b = bin(i)[2:].zfill(N)
        party = [j for j, e in enumerate(b) if e == '1']
        if len(party) == 1:    continue

        flg = True
        for p1 in party:
            for p2 in party:
                if p1 == p2:    continue
                if not path[p1][p2]:
                    flg = False
                    break
            else:
                continue
            break

        if flg:
            res = max(res, len(party))

    print(res)


if __name__ == '__main__':
    main()
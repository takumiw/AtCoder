def main():
    N = int(input())
    inp = [list(map(int, input().split())) for _ in range(N)]

    for cx in range(0, 101):
        for cy in range(0, 101):
            hmax = 10 ** 10
            ha = 0
            for x, y, h in inp:
                m = abs(x-cx) + abs(y-cy)
                if h == 0:
                    hmax = min(hmax, m)
                else:
                    ht = m + h
                    if ht < 1:
                        ha = 0
                        break
                    if ha:
                        if ht != ha:
                            ha = 0
                            break
                    else:
                        ha = ht
            
            if 0 < ha <= hmax:
                print(cx, cy, ha)
                exit()


if __name__ == "__main__":
    main()
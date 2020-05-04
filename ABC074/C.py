import sys
readline = sys.stdin.readline

def main():
    A, B, C, D, E, F = map(int, readline().rstrip().split())
    X = set()
    for a in range(F//(100*A)+1):
        for b in range(F//(100*B)+1):
            if 100 * a * A + 100 * b * B <= F:
                X.add(100 * a * A + 100 * b * B)
    X.remove(0)

    Y = set()
    for c in range(F//C+1):
        for d in range(F//D+1):
            if c * C + d * D <= F/2:
                Y.add((c * C + d * D))

    ans = (0, 0)
    max_dens = -1
    for x in X:
        for y in Y:
            if x + y > F:
                continue
            if y * 100 <= x * E:
                dens = y/(x+y)
                if dens > max_dens:
                    ans = (x+y, y)
                    max_dens = dens
    print(*ans)

if __name__ == '__main__':
    main()
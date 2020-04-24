import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    S = [readline().rstrip() for _ in range(N)]
    alp = list('abcdefghijklmnopqrstuvwxyz')
    d = {a: 100 for a in alp}
    for s in S:
        for w in alp:
            if w in s:
                d[w] = min(d[w], s.count(w))
            else:
                d[w] = 0

    d = sorted(d.items())
    for k, v in d:
        if v == 100:
            continue
        print(k * v, end='')


if __name__ == '__main__':
    main()
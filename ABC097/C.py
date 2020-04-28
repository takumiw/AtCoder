import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip()
    K = int(readline())
    N = len(S)
    d = {}
    for i in range(N):
        s = ''
        head = S[i]
        d.setdefault(head, set())
        for j in range(i, min(N, i+5)):
            s += S[j]
            d[head].add(s)

    for key, val in sorted(d.items()):
        if K <= len(val):
            print(sorted(list(val))[K-1])
            return
        else:
            K -= len(val)


if __name__ == '__main__':
    main()
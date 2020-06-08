import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    T = [int(readline()) for _ in range(N)]
    s = sum(T)
    res = 10 ** 10
    for i in range(2**N):
        b = bin(i)[2:]
        a = sum([T[i] for i, e in enumerate(b) if e == '1'])
        res = min(res, max(a, s - a))

    print(res)

if __name__ == '__main__':
    main()
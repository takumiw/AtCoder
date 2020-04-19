import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    d = {}
    for i, a in enumerate(A):
        if a in d.keys():
            d[a] += 1
        else:
            d[a] = 1

    for i in range(1, N+1):
        if i in d.keys():
            print(d[i])
        else:
            print(0)


if __name__ == '__main__':
    main()
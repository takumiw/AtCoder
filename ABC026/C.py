import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    B = [[] for _ in range(N)]
    for i in range(1, N):
        b = int(readline())
        B[b-1].append((i))
    
    p = [-1] * N
    for i in range(N-1, -1, -1):
        if len(B[i]) == 0:
            p[i] = 1
        else:
            bp = [p[b] for b in B[i]]
            p[i] = max(bp) + min(bp) + 1

    print(p[0])


if __name__ == '__main__':
    main()
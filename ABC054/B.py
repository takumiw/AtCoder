import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    A = [readline().rstrip() for _ in range(N)]
    B = [readline().rstrip() for _ in range(M)]
    if A == B:
        print('Yes')
        return
    for h in range(N-M):
        for w in range(N-M):
            a = [l[w:w+M] for l in A[h:h+M]]
            if a == B:
                print('Yes')
                return

    print('No')

if __name__ == '__main__':
    main()
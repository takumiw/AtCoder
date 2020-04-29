import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    ans = -10 ** 4
    for i in range(N):
        scr_t = -10 ** 4
        scr_a = -10 ** 4
        for j in range(N):
            if i == j:
                continue
            if i < j:
                T = A[i:j+1]
            else:
                T = A[j:i+1]
            st = sum([t for i, t in enumerate(T) if i % 2 == 0])
            sa = sum([t for i, t in enumerate(T) if i % 2 == 1])
            if sa > scr_a:
                scr_a = sa
                scr_t = st
        
        ans = max(ans, scr_t)
    
    print(ans)


if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    ans = 0
    cnt = 0
    j = 0
    for i in range(N):
        while j < N:
            cnt += A[j]
            if cnt >= K:
                ans += N - j
                cnt -= A[i]
                cnt -= A[j]
                break
            j += 1
    
    print(ans)

if __name__ == '__main__':
    main()
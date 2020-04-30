import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    S = [A[0]]
    for i in range(1, N):
        S.append(S[i-1] + A[i])

    ans = 0
    S.append(0)
    for i in range(N-K+1):
        ans += S[i+K-1] - S[i-1]
    
    print(ans)

if __name__ == '__main__':
    main()
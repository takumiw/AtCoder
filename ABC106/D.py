import sys
readline = sys.stdin.readline

def main():
    N, M, Q = map(int, readline().rstrip().split())
    train_cnt = [[0] * N for _ in range(N)]
    for _ in range(M):
        l, r = map(int, readline().rstrip().split())
        train_cnt[l-1][r-1] += 1
    
    for i in range(N):
        for j in range(1, N):
            train_cnt[i][j] += train_cnt[i][j-1]
    
    for j in range(N):
        for i in range(N-2, -1, -1):
            train_cnt[i][j] += train_cnt[i+1][j]
    
    for _ in range(Q):
        p, q = map(int, readline().rstrip().split())
        print(train_cnt[p-1][q-1])


if __name__ == '__main__':
    main()
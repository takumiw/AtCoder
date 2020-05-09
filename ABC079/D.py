import sys
readline = sys.stdin.readline

def main():
    H, W = map(int, readline().rstrip().split())
    C = [list(map(int, readline().rstrip().split())) for _ in range(10)]
    for k in range(10):
        for i in range(10):
            for j in range(10):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])

    A = [tuple(map(int, readline().rstrip().split())) for _ in range(H)]
    cost = 0
    for h in range(H):
        for w in range(W):
            a = A[h][w]
            if 0 <= a <= 9:
                cost += C[a][1]
    
    print(cost)

if __name__ == '__main__':
    main()
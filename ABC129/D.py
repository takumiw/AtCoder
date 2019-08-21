def main():
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    count_matrix = [[0 for _ in range(W)] for _ in range(H)]

    # 横方向についてカウントする
    for i in range(H):
        start = 0
        count = 0
        for j in range(W):
            s = matrix[i][j]
            if s == '.':
                count += 1
                if j == W-1:
                    for k in range(start, j+1):
                        count_matrix[i][k] += count
            else:
                for k in range(start, j):
                    count_matrix[i][k] += count
                start = j+1
                count = 0

    # 縦方向についてカウントする
    for i in range(W):
        start = 0
        count = 0
        for j in range(H):
            s = matrix[j][i]
            if s == '.':
                count += 1
                if j == H-1:
                    for k in range(start, j+1):
                        count_matrix[k][i] += count
            else:
                for k in range(start, j):
                    count_matrix[k][i] += count
                start = j+1
                count = 0
    
    max_val = 0
    for i in range(H):
        for j in range(W):
            max_val = max(max_val, count_matrix[i][j])
    print(max_val-1)
    return

if __name__ == '__main__':
    main()
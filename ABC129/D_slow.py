def main():
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    L = [[0 for _ in range(W)] for _ in range(H)]
    R = [[0 for _ in range(W)] for _ in range(H)]
    D = [[0 for _ in range(W)] for _ in range(H)]
    U = [[0 for _ in range(W)] for _ in range(H)]

    # 左方向についてカウントする
    for i in range(H):
        if matrix[i][0] == '.':
            L[i][0] = 1
        for j in range(1, W):
            s = matrix[i][j]
            if s == '.':
                L[i][j] = L[i][j-1] + 1

    # 右方向についてカウントする
    for i in range(H):
        if matrix[i][-1] == '.':
            R[i][-1] = 1
        for j in range(W-2, -1, -1):
            s = matrix[i][j]
            if s == '.':
                R[i][j] = R[i][j+1] + 1
    
    # 上方向についてカウントする
    for i in range(W):
        if matrix[0][i] == '.':
            U[0][i] = 1
        for j in range(1, H):
            s = matrix[j][i]
            if s == '.':
                U[j][i] = U[j-1][i] + 1
    
    # 下方向についてカウントする
    for i in range(W):
        if matrix[-1][i] == '.':
            D[-1][i] = 1
        for j in range(H-2, -1, -1):
            s = matrix[j][i]
            if s == '.':
                D[j][i] = D[j+1][i] + 1
    
    max_val = -3
    for i in range(H):
        for j in range(W):
            max_val = max(max_val, R[i][j]+L[i][j]+U[i][j]+D[i][j])
    print(max_val-3)
    return

if __name__ == '__main__':
    main()
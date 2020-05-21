import sys
readline = sys.stdin.readline

def main():
    x, y, W = readline().rstrip().split()
    mat = tuple(tuple(readline().rstrip()) for _ in range(9))
    res = ''
    w_pre, h_pre = int(x) - 1, int(y) - 1
    for _ in range(4):
        res += mat[h_pre][w_pre]
        if W == 'R':
            if w_pre == 8:
                w_pre = 7
                W = 'L'
            else: 
                w_pre += 1
        elif W == 'L':
            if w_pre == 0:
                w_pre = 1
                W = 'R'
            else: 
                w_pre -= 1
        elif W == 'U':
            if h_pre == 0:
                h_pre = 1
                W = 'D'
            else:
                h_pre -= 1
        elif W == 'D':
            if h_pre == 8:
                h_pre = 7
                W = 'U'
            else:
                h_pre += 1
        elif W == 'RU':
            if h_pre == 0 and w_pre == 8:
                W = 'LD'
                h_pre, w_pre = 1, 7
            elif w_pre == 8:
                h_pre -= 1
                w_pre = 7
                W = 'LU'
            elif h_pre == 0:
                h_pre = 1
                w_pre += 1
                W = 'RD'
            else:
                h_pre -= 1
                w_pre += 1
        elif W == 'RD':
            if h_pre == 8 and w_pre == 8:
                W = 'LU'
                h_pre, w_pre = 7, 7
            elif w_pre == 8:
                h_pre += 1
                w_pre = 7
                W = 'LD'
            elif h_pre == 8:
                h_pre = 7
                w_pre += 1
                W = 'RU'
            else:
                h_pre += 1
                w_pre += 1
        elif W == 'LU':
            if h_pre == 0 and w_pre == 0:
                W = 'RD'
                h_pre, w_pre = 1, 1
            elif w_pre == 0:
                h_pre -= 1
                w_pre = 1
                W = 'RU'
            elif h_pre == 0:
                h_pre = 1
                w_pre -= 1
                W = 'LD'
            else:
                h_pre -= 1
                w_pre -= 1
        elif W == 'LD':
            if h_pre == 8 and w_pre == 0:
                W = 'RU'
                h_pre, w_pre = 7, 1
            elif w_pre == 0:
                h_pre += 1
                w_pre = 1
                W = 'RD'
            elif h_pre == 8:
                h_pre = 7
                w_pre -= 1
                W = 'LU'
            else:
                h_pre += 1
                w_pre -= 1
    
    print(res)

if __name__ == '__main__':
    main()
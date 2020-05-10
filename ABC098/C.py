import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    S = readline().rstrip()
    e_right = S.count('E')
    w_left = 0
    res = N
    
    for i in range(N):
        if S[i] == 'E':
            e_right -= 1
            res = min(res, e_right + w_left)
        else:
            res = min(res, e_right + w_left)
            w_left += 1
    
    print(res)

if __name__ == '__main__':
    main()
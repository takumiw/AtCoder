import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip()
    T = readline().rstrip()
    N = len(S)
    M = len(T)
    for i in range(N-M, -1, -1):
        s = S[i:i+M]
        flg = True
        for e1, e2 in zip(s, T):
            if e1 != '?' and e1 != e2:
                flg = False
                break
        if flg:
            ans = list(S)
            for j in range(i, i+M):
                ans[j] = T[j-i]
            ans = ''.join(ans)
            print(ans.replace('?', 'a'))
            return

    print('UNRESTORABLE')


if __name__ == '__main__':
    main()
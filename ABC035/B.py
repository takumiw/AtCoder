import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip()
    T = int(readline())
    cnt_l = S.count('L')
    cnt_r = S.count('R')
    cnt_u = S.count('U')
    cnt_d = S.count('D')
    cnt_q = S.count('?')
    if T == 1:
        print(abs(cnt_l-cnt_r) + abs(cnt_u-cnt_d) + cnt_q)
    else:
        d = abs(cnt_l-cnt_r) + abs(cnt_u-cnt_d)
        if d - cnt_q < 0:
            if (d - cnt_q) % 2 == 1:
                d = 1
            else:
                d = 0
        else:
            d -= cnt_q
        print(d)

if __name__ == '__main__':
    main()
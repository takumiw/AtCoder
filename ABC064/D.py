import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    S = readline().rstrip()
    res = S[:]

    pls_left = 0
    pls_right = 0
    for s in S:
        if s == '(':
            pls_right += 1
        else:
            if pls_right == 0:
                pls_left += 1
            else:
                pls_right -= 1

    res = '(' * pls_left + S + ')' * pls_right

    print(res)

if __name__ == '__main__':
    main()
import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    S1 = readline().rstrip()
    S2 = readline().rstrip()
    if S1[0] == S2[0]:
        cnt = 3
        i = 1
        pre = 'x'
    else:
        cnt = 6
        i = 2
        pre = 'y'
    while i < N:
        if S1[i] == S2[i]:
            next = 'x'
        else:
            next = 'y'
        if pre == next == 'x':
            cnt *= 2
            i += 1
        elif pre == next == 'y':
            cnt *= 3
            i += 2
        elif pre == 'x' and next == 'y':
            cnt *= 2
            i += 2
        else:
            i += 1
        pre = next

    print(cnt % MOD)


if __name__ == '__main__':
    main()
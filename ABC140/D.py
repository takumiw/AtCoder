N, K = map(int, input().split())
S = input()

def solve():
    global K, S
    concat_S = S[:]
    while 'LL' in concat_S:
        concat_S = concat_S.replace('LL', 'L')
    while 'RR' in concat_S:
        concat_S = concat_S.replace('RR', 'R')

    ans = len(S) - len(concat_S)
    if len(concat_S) >= 4:
        # 2個ずつ消す
        num_rm = min(K, (len(concat_S)-2)//2)
        K -= num_rm
        ans += num_rm * 2
        len_concat_S = len(S) - ans

        if K:
            if len_concat_S == 3:
                ans += 2
            elif len_concat_S == 2:
                ans += 1
        print(ans)
        return
    if K:
        if len(concat_S) == 3:
            ans += 2
        elif len(concat_S) == 2:
            ans += 1
        
    print(ans)
    return

if __name__ == "__main__":
    solve()
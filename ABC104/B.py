S = input()
if S[0] == 'A' and S[2:-1].count('C') == 1:
    S = S[1] + S[2:-1].replace('C', '') + S[-1]
    if S == S.lower():
        print('AC')
        exit()
print('WA')
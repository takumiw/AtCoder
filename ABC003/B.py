S = input()
T = input()
for s, t in zip(S, T):
    if s == t:
        continue
    if s == '@' and t in list('atcoder'):
        continue
    elif t == '@' and s in list('atcoder'):
        continue
    else:
        print('You will lose')
        exit()
    

print('You can win')
S = input()

S = S.replace('eraser', '')
S = S.replace('erase', '')
S = S.replace('dreamer', '')
S = S.replace('dream', '')

if len(S) == 0:
    print('YES')
else:
    print('NO')
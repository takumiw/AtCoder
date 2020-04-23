S = input()
alp = set(list('abcdefghijklmnopqrstuvwxyz'))
alp -= set(S)
if len(alp) == 0:
    print('None')
else:
    print(sorted(list(alp))[0])
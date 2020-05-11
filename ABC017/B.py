X = input()
while X:
    if X[0] in list('oku'):
        X = X[1:]
    elif X[:2] == 'ch':
        X = X[2:]
    else:
        print('NO')
        exit()

print('YES')
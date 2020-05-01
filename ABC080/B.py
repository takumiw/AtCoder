X = input()
if int(X) % sum(list(map(int, list(X)))) == 0:
    print('Yes')
else:
    print('No')
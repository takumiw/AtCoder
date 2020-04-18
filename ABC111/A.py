n = input()
ans = []
for nn in n:
    if nn == '1':
        print(9, end='')
    elif nn == '9':
        print(1, end='')
    else:
        print(nn, end='')
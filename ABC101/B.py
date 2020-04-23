N = input()
S = sum(list(map(int, list(N))))
if int(N) % S == 0:
    print('Yes')
else:
    print('No')
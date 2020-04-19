S = list(input())
T = list(input())

if S == T:
        print('Yes')
        exit()

for _ in range(len(S)):
    S = S[-1:] + S[:-1]
    if S == T:
        print('Yes')
        exit()

print('No')
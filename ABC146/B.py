N = int(input())
S = input()

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
di = {}
for i in range(len(alp)):
    di[alp[i]] = i
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# N = N % len(S)

ans = []
for s in S:
    ans.append(alp[di[s]+N])

print(''.join(ans))
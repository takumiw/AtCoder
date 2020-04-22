S = input()
ans = []
for s in list('ABCDEF'):
    ans.append(S.count(s))

print(*ans)
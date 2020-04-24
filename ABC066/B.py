S = input()
ans = 0
for i in range(2, len(S), 2):
    s = S[:i]
    if s[:i//2] == s[i//2:]:
        ans = i

print(ans)
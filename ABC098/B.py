N = int(input())
S = input()
res = 0
for i in range(1, N-1):
    a, b = S[:i], S[i:]
    res = max(res, len(list(set(a) & set(b))))

print(res)
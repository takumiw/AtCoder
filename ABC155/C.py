from collections import Counter
N = int(input())
S = [input() for _ in range(N)]

c = Counter(S).most_common()
cnt_max = c[0][1]
ans = []
for s, cnt in c:
    if cnt != cnt_max:
        break
    ans.append(s)

print('\n'.join(sorted(ans)))
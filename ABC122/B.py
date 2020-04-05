import re

S = input()
S = re.sub('[^ACGT]', '_', S)
S = S.split('_')
ans = 0
for s in S:
    ans = max(ans, len(s))
print(ans)
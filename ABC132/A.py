from collections import Counter
s = list(input())
c = Counter(s)
if len(c) == 2 and c.most_common()[0][1] == 2:
    print('Yes')
else:
    print('No')
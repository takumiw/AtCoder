N = int(input())

cand = set([i * j for i in range(1,10) for j in range(1, 10)])
if N in cand:
    print('Yes')
else:
    print('No')
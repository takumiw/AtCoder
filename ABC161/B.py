N, M = map(int, input().split())
A = list(map(int, input().split()))

thr =  sum(A) / (4 * M)
A = [a for a in A if a >= thr]
if len(A) >= M:
    print('Yes')
else:
    print('No')
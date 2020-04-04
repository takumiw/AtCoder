N = int(input())
A = list(map(int, input().split()))

A = [a for i, a in enumerate(A) if a <= i+1]

k = 0
for a in A:
    if a == k+1:
        k += 1
    

if k == 0:
    print(-1)
else:
    print(N - k)
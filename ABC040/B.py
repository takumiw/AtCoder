from math import floor

N = int(input())
ans = N
for a in range(1, floor(N**(1/2))+1):
    b = N // a
    ans = min(ans, (b-a) + N - a*b)
print(ans)
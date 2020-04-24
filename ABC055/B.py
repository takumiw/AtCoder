n = int(input())
ans = 1
mod = 10 ** 9 + 7
for i in range(1, n+1):
    ans = (ans * i) % mod

print(ans)
s = input()
n = len(s)
k = int(input())
ans = set()
for i in range(n-k+1):
    ans.add(s[i:i+k])

print(len(ans))
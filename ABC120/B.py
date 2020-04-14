A, B, K = map(int, input().split())

ans = [1]
for i in range(2, A+1):
    if A % i == 0 and B % i == 0:
        ans.append(i)

print(ans[-K])
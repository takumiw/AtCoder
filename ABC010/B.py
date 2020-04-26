N = int(input())
A = list(map(int, input().split()))
2, 4, 5, 6, 8
ans = 0
for a in A:
    if a == 8 or a == 2:
        ans += 1
    elif 4 <= a <= 6:
        ans += a - 3

print(ans)
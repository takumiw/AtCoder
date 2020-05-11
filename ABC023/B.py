N = int(input())
S = input()
ans = 'b'
for i in range(1, 200):
    if len(ans) >= N:
        break
    if i % 3 == 1:
        ans = 'a' + ans + 'c'
    elif i % 3 == 2:
        ans = 'c' + ans + 'a'
    else:
        ans = 'b' + ans + 'b'

if ans == S:
    print(i-1)
else:
    print(-1)
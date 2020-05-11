N, A, B = map(int, input().split())
ans = 0
for _ in range(N):
    s, d = input().split()
    if s == 'East':
        ans -= min(max(int(d), A), B)
    else:
        ans += min(max(int(d), A), B)

if ans == 0:
    print(0)
elif ans < 0:
    print('East', abs(ans))
else:
    print('West', ans)
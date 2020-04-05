N, Q = map(int, input().split())
S = input()
cnt = [0] * N

for i in range(1, N):
    if S[i-1:i+1] == 'AC':
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]

ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(cnt[r-1] - cnt[l-1])

print('\n'.join(list(map(str, ans))))
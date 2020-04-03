N, M = map(int, input().split())
S, C = [], []
for _ in range(M):
    s, c = map(int, input().split())
    s -= 1
    if s in S:
        if C[S.index(s)] != c:
            print(-1)
            exit()
        else:
            continue
    S.append(s)
    C.append(c)

if len(S) == 0:
    if N == 1:
        print(0)
    elif N == 2:
        print(10)
    else:
        print(100)
    exit()

ans = [-1] * N
for i in range(len(S)):
    ans[S[i]] = C[i]

if N == 1:
    if ans[0] == 0:
        print(0)
        exit()

if ans[0] == -1:
    ans[0] = 1
elif ans[0] == 0:
    print(-1)
    exit()

ans = [a if a != -1 else 0 for a in ans]
print(''.join(list(map(str, ans))))
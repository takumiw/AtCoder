N = int(input())
S = []
P = []
for _ in range(N):
    s, p = input().split()
    S.append(s)
    P.append(int(p))

po = sum(P)
for s, p in zip(S, P):
    if p > po / 2:
        print(s)
        exit()

print('atcoder')
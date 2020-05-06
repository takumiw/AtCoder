N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))
if a in P or b in P or len(set(P)) != len(P):
    print('NO')
else:
    print('YES')
N = int(input())
P = list(map(int, input().split()))

cnt = sum([p1 != p2 for p1, p2 in zip(P, sorted((P)))])
if cnt <= 2:
    print('YES')
else:
    print('NO')
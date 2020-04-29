a, b, c, d = map(int, input().split())
r1, r2 = b/a, d/c
if r1 > r2:
    print('TAKAHASHI')
elif r1 < r2:
    print('AOKI')
else:
    print('DRAW')
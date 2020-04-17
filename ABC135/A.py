A, B = map(int, input().split())

ans = abs(A+B)
if ans % 2 == 0:
    print(ans // 2)
else:
    print('IMPOSSIBLE')
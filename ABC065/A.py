x, a, b = map(int, input().split())
e = b - a
if e <= 0:
    print('delicious')
elif e <= x:
    print('safe')
else:
    print('dangerous')
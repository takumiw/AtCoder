a, b = map(int, input().split())
l = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
if a == b:
    print('Draw')
elif l.index(a) < l.index(b):
    print('Bob')
else:
    print('Alice')
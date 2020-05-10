a, b = input().split()
v = int(a+b) ** (1/2)
if v.is_integer():
    print('Yes')
else:
    print('No')
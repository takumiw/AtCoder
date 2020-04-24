w, a, b = map(int, input().split())
if b > a + w:
    print(b - a - w)
elif a > b + w:
    print(a - b - w)
else:
    print(0)
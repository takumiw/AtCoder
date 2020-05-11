a = int(input())
b = int(input())
if a > b:
    print(min(a-b, 10-a+b))
else:
    print(min(b-a, 10-b+a))
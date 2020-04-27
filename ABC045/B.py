Sa = list(input())
Sb = list(input())
Sc = list(input())

n = 'a'
while True:
    if n == 'a':
        if not len(Sa):
            ans = 'A'
            break
        n = Sa.pop(0)
    elif n == 'b':
        if not len(Sb):
            ans = 'B'
            break
        #ans = 'B'
        n = Sb.pop(0)
    else:
        if not len(Sc):
            ans = 'C'
            break
        #ans = 'C'
        n = Sc.pop(0)
    # print(n, ans)

print(ans)
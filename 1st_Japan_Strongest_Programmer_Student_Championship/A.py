M, D = map(int, input().split())


s = 0
for i in range(1, M+1):
    for j in range(22, D+1):
        if int(str(j)[0]) < 2 or int(str(j)[1]) < 2:
            continue
        d10 = str(j)[0]
        d1 = str(j)[1]
        if int(d10) * int(d1) == i:
            s += 1
print(s)
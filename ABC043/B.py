S = input()
d = []
for s in S:
    if s == '0' or s == '1':
        d.append(s)
    else:
        d = d[:-1]

print(*d, sep='')
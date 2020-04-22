n = int(input())
s = sum([i * j for i in range(1, 10) for j in range(1, 10)])
sn = s - n
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == sn:
            print('{} x {}'.format(i, j))
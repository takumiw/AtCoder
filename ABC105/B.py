n = int(input())
for i in range(30):
    for j in range(20):
        if i * 4 + j * 7 == n:
            print('Yes')
            exit()

print('No')
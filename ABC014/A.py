a = int(input())
b = int(input())
for x in range(1000):
    if (a + x) % b == 0:
        print(x)
        exit()
A, B = map(int, input().split())

tap = 1
count = 0
while tap < B:
    tap += (A-1)
    count += 1
print(count)
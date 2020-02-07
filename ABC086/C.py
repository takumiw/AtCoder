N = int(input())
t, x, y = 0, 0, 0

for _ in range(N):
    ti, xi, yi = map(int, input().split())
    dt, dx, dy = ti - t, abs(xi - x), abs(yi - y)
    t, x, y = ti, xi, yi
    if ((dt - (dx + dy)) % 2 != 0) or (dx + dy > dt):
        print('No')
        exit()

print('Yes')
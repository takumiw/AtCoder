x, y, z = map(int, input().split())
ans = 0
x -= 2 * z
while x >= y:
    x -= y
    ans += 1
    x -= z
print(ans)
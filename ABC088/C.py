grid = [list(map(int, input().split())) for _ in range(3)]
ans = 'Yes'

b1 = 0
a1 = grid[0][0]
a2 = grid[1][0]
a3 = grid[2][0]

b2 = grid[0][1] - a1
b3 = grid[0][2] - a1

if b2 + a2 != grid[1][1]:
    ans = 'No'

if b2 + a3 != grid[2][1]:
    ans = 'No'

if b3 + a2 != grid[1][2]:
    ans = 'No'

if b3 + a3 != grid[2][2]:
    ans = 'No'

print(ans)
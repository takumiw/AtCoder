import math
N = int(input())
POINTS = [tuple(map(int, input().split())) for _ in range(N)]
longest = 0
for i in range(N):
    x1, y1 = POINTS[i]
    for j in range(i+1, N):
        x2, y2 = POINTS[j]
        longest = max(longest, math.sqrt((x2-x1)**2 + (y2-y1)**2))
print(longest)
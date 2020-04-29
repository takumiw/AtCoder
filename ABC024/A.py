a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
ans = s * a + t * b
if s + t >= k:
    ans -= (s+t) * c
print(max(ans, 0))
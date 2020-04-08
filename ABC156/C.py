from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
N = int(input())
X = list(map(int, input().split()))

p = sum(X) / N
p = Decimal(str(p)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
ans = 0
for x in X:
    ans += (x - p) ** 2

print(ans)
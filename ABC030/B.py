n, m = map(int, input().split())

n = (n % 12 + m / 60) * 30
m = m * 6
print(min(abs(n-m), 360-abs(n-m)))
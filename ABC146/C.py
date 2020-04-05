A, B, X = map(int, input().split())

min_n = 0
max_n = 10**9 + 1

while abs(max_n - min_n) > 1:
    half = (max_n + min_n) // 2
    if A * half + B * len(str(half)) <= X:
        min_n = half
    else:
        max_n = half

print(min_n)
N = int(input())
A = list(map(int, input().split()))

min_div = 10 ** 9 
for a in A:
    div_count = 0
    while a % 2 == 0:
        a /= 2
        div_count += 1
    min_div = min(min_div, div_count)

print(min_div)
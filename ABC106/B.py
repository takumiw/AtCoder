def make_divisors(n) -> list:
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

N = int(input())
cnt = 0
for i in range(105, N+1, 2):
    if len(make_divisors(i)) == 8:
        cnt += 1

print(cnt)
import fractions
import math

A, B = map(int, input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def is_prime(x):
    if x < 2: return False # 2未満に素数はない
    if x == 2 or x == 3 or x == 5: return True # 2,3,5は素数
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False # 2,3,5の倍数は合成数
    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0: return False
        prime += step
        step = 6 - step
    return True

def solve():
    gcd = fractions.gcd(A, B)
    divisors = make_divisors(gcd)
    l = [x for x in divisors if is_prime(x)]
    print(len(l)+1)

if __name__ == '__main__':
    solve()
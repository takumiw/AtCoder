a, b, c = map(int, input().split())
mod = 10 ** 9 + 7
print(((a%mod) * (b%mod) * (c%mod)) % mod)
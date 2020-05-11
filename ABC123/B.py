inp = [int(input()) for _ in range(5)]
rem = [p % 10 if p % 10 != 0 else 10 for p in inp]
idx = rem.index(min(rem))
min_rem = inp[idx]
res = 0
inp.remove(min_rem)
for a in inp:
    if a % 10 == 0:
        res += a
    else:
        res += a + (10 - a % 10)

print(res + min_rem)
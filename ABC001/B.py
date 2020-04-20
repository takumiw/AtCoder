m = int(input())
m *= 0.001
if m < 0.1:
    ans = '00'
elif m <= 5:
    ans = int(m * 10)
elif m <= 30:
    ans = int(m + 50)
elif m <= 70:
    ans = int((m-30) // 5 + 80)
else:
    ans = 89

print(str(ans).zfill(2))
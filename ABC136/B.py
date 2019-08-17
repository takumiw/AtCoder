import sys

N = int(input())
digit = len(str(N))
# 1-99
if digit < 3:
    print(min((N), 9))
# 100-999
elif digit == 3:
    print(N-99+9)
# 1000-9999
elif digit == 4:
    print(999-99+9)
# 10000-99999
elif digit == 5:
    print(N-9999-99+999+9)
# 100000
else:
    print(99999-9999-99+999+9)
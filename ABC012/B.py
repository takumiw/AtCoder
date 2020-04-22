n = int(input())
h = n // 60 // 60
n -= h * 60 * 60
m = n // 60
n -= m * 60
print('{}:{}:{}'.format((str(h)).zfill(2), (str(m)).zfill(2), (str(n)).zfill(2)))
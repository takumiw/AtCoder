X = int(input())
ureshisa = (X // 500) * 1000
X = X % 500 
ureshisa += (X // 5) * 5
print(ureshisa)
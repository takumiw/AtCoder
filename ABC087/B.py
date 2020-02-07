A = int(input())  # 500円玉の枚数
B = int(input())  # 100円玉の枚数
C = int(input())  # 50円玉の枚数
X = int(input())  # 合計X円にしたい

ans = 0
for a in range(min(A+1, X//500+1)):
    x = X - 500 * a
    for b in range(min(B+1, X//100+1)):
        xx = x - 100 * b
        if (xx/50).is_integer() and xx//50 <= C and xx//50 >= 0:
            ans += 1
            
print(ans)
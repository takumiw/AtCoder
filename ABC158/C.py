import math
A, B = map(int, input().split())

Xa_max = (A + 1) / 0.08
Xa_min = (A) / 0.08

Xb_max = (B + 1) / 0.1
Xb_min = (B) / 0.1

# 範囲が被らない場合
if Xa_min >= Xb_max or Xb_min >= Xa_max:
    print(-1)
    exit()

if Xa_min >= Xb_min:
    ans = math.ceil(Xa_min)
    if ans >= Xb_max:
        print(-1)
        exit()
else:
    ans = math.ceil(Xb_min)
    if ans >= Xa_max:
        print(-1)
        exit()

print(ans)
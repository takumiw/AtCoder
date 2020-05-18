INF = 2 * 10 ** 12

A, K = map(int, input().split())
if K == 0:
    print(INF - A)
else:
    now = A
    res = 0
    while now < INF:
        now += 1 + K * now
        res += 1
    
    print(res)
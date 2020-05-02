a, b, c, d = map(int, input().split())
al = set([i for i in range(a, b)])
bo = set([i for i in range(c, d)])
print(len(al&bo))
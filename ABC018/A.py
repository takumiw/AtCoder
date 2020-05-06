l = [int(input()) for _ in range(3)]
ll = sorted(l, reverse=True)
for e in l:
    print(ll.index(e)+1)
O = input()
E = input()
if len(O) > len(E):
    for o, e in zip(O[:-1], E):
        print(o + e, end='')
    print(O[-1])
else:
    for o, e in zip(O, E):
        print(o + e, end='')
N = int(input())
V = list(map(int, input().split()))
V.sort()
while len(V) > 1:
    V.append((V[0]+V[1])/2)
    V.pop(0)
    V.pop(0)
    V.sort()
print(V[0])
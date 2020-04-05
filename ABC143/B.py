N = int(input())
D = list(map(int, input().split()))
s = 0

for i in range(N):
    for j in range(i+1, N):
        s += D[i] * D[j]

print(s)
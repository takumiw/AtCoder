K, S = map(int, input().split())
count = 0
for X in range(K+1):
    for Y in range(K+1):
        if S-X-Y >= 0 and S-X-Y <= K:
            count += 1
print(count)
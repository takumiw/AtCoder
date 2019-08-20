S = list(input())
N = len(S)
counter = [0]*N

# Rについて、左から右に順に数えていく
start = 0
even, odd = 0, 0
for i, s in enumerate(S):
    if s == 'R':
        if (i-start) % 2 == 0:
            even += 1
        else:
            odd += 1
    else:
        if even > 0 or odd > 0:
            if (i-start) % 2 == 0:
                counter[i] += even
                counter[i-1] += odd
            else:
                counter[i] += odd
                counter[i-1] += even
            even, odd = 0, 0
        start = i

# Lについて、右から左に順に数えていく
start = 0
even, odd = 0, 0
for i, s in enumerate(S[::-1]):
    if s == 'L':
        if (i-start) % 2 == 0:
            even += 1
        else:
            odd += 1
    else:
        if even > 0 or odd > 0:
            if (i-start) % 2 == 0:
                counter[N-1-i] += even
                counter[N-i] += odd
            else:
                counter[N-1-i] += odd
                counter[N-i] += even
            even, odd = 0, 0
        start = i

print(' '.join(list(map(str, counter))))
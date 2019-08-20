S = list(input())
N = len(S)

# Rについて、左から右に順に数えていく
r_counter = [0]*N
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
                r_counter[i] += even
                r_counter[i-1] += odd
            else:
                r_counter[i] += odd
                r_counter[i-1] += even
            even, odd = 0, 0
        start = i

# Lについて、右から左に順に数えていく
l_counter = [0]*N
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
                l_counter[i] += even
                l_counter[i-1] += odd
            else:
                l_counter[i] += odd
                l_counter[i-1] += even
            even, odd = 0, 0
        start = i

for i, j in zip(r_counter, l_counter[::-1]):
    print(i+j, end=' ')
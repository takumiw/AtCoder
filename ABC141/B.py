S = list(input())

is_easy = True
for i in range(len(S)):
    if i % 2 == 1:
        if S[i] not in ['L', 'U', 'D']:
            is_easy = False
    if i % 2 == 0:
        if S[i] not in ['R', 'U', 'D']:
            is_easy = False

if is_easy:
    print('Yes')
else:
    print('No')
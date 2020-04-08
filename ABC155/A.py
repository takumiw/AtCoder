A, B, C = map(int, input().split())

if (A == B and B != C) or (A == C and B != C) or (C == B and A != C):
    print('Yes')
else:
    print('No')
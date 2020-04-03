A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

if (A[0][0] in b) and (A[0][1] in b) and (A[0][2] in b) or \
    (A[1][0] in b) and (A[1][1] in b) and (A[1][2] in b) or \
    (A[2][0] in b) and (A[2][1] in b) and (A[2][2] in b) or \
    (A[0][0] in b) and (A[0][1] in b) and (A[0][2] in b) or \
    (A[0][0] in b) and (A[1][0] in b) and (A[2][0] in b) or \
    (A[0][1] in b) and (A[1][1] in b) and (A[2][1] in b) or \
    (A[0][2] in b) and (A[1][2] in b) and (A[2][2] in b) or \
    (A[0][0] in b) and (A[1][1] in b) and (A[2][2] in b) or \
    (A[0][2] in b) and (A[1][1] in b) and (A[2][0] in b):
    print('Yes')
else:
    print('No')
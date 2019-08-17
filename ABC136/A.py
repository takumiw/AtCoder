A, B, C = map(int, input().split())
print(max(C - (A - min(A, B)), 0))
N = int(input())
A = list(set([int(input()) for _ in range(N)]))
print(sorted(A, reverse=True)[1])
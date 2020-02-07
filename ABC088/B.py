N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

points_alice = 0
points_bob = 0
for i in range(0, N, 2):
    points_alice += A[i]

for i in range(1, N, 2):
    points_bob += A[i]

print(points_alice - points_bob)
N = int(input())
B = list(map(int, input().split()))
b_max = max(B)
A = [b_max for _ in range(N)]

def solve():
    for i, b in enumerate(B):
        A[i] = min(A[i], b)
        A[i+1] = min(A[i+1], b)
    print(sum(A))

if __name__ == "__main__":
    solve()
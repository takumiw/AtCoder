N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

def solve():
    m = A.pop(0)
    ans = B[m-1]
    for i, a in enumerate(A):
        ans += B[a-1]
        if a == m + 1:
            ans += C[m-1]
        m = a
    print(ans)

if __name__ == "__main__":
    solve()
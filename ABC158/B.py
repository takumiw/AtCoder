N, A, B = map(int, input().split())

n_pairs = N // (A + B)
ans = n_pairs * A
N -= n_pairs * (A + B)
ans += min(N, A)
print(ans)
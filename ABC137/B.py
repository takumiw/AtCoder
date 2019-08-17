K, X = map(int, input().split())
print(' '.join([str(i) for i in range(X-K+1, X+K)]))
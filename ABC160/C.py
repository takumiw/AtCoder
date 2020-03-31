def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    max_diff = A[0] + (K - A[-1])
    for i in range(len(A)-1):
        max_diff = max(max_diff, A[i+1] - A[i])
    
    print(K - max_diff)

if __name__ == '__main__':
    main()
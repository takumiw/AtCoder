def main():
    N, M = map(int, input().split())
    left, right = 0, N-1
    for _ in range(M):
        l, r = map(int, input().split())
        left = max(left, l-1)
        right = min(right, r-1)
    
    print(max(0, right - left + 1))

if __name__ == "__main__":
    main()
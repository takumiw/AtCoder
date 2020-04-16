def main():
    N, M = map(int, input().split())
    cnts = [0 for _ in range(M)]
    for _ in range(N):
        A = list(map(int, input().split()))
        K = A.pop(0)
        for a in A:
            cnts[a-1] += 1
    
    ans = cnts.count(N)
    print(ans)


if __name__ == "__main__":
    main()
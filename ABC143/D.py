from bisect import bisect_left

def main():
    N = int(input())
    L = list(map(int, input().split()))
    
    L.sort()
    ans = 0
    for i in range(N-2):
        a = L[i]
        for j in range(i+1, N-1):
            k = bisect_left(L, a + L[j])
            ans += (k - (j + 1))

    print(ans)

    
if __name__ == "__main__":
    main()
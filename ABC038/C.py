import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    ans = N
    i = 0
    A.append(-1)
    while i < N:
        ai = A[i]
        l = 1
        for j in range(i+1, N+1):
            if ai < A[j]:
                ai = A[j]
                l += 1
            else:
                ans += (l-1) * l // 2
                i = j
                break
        if j == N+1:
            break

    print(ans)


if __name__ == '__main__':
    main()
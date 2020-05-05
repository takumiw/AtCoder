import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    ave = sum(A) / N
    if ave.is_integer() == False:
        print(-1)
    else:
        ans = 0
        for i in range(N-1):
            if A[i] != ave:
                A[i+1] = A[i+1] + (A[i] - ave)
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()
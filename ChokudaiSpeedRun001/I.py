import sys
readline = sys.stdin.readline


def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    res = 0
    cnt = 0
    j = 0
    for i in range(N):
        while j < N:
            cnt += A[j]
            if cnt == N:
                res += 1
            if cnt >= N:
                cnt -= A[i]
                cnt -= A[j]
                if i == j:
                    j += 1
                    cnt += A[i]
                break
            j += 1
        if j == N:
            break
    
    print(res)


if __name__ == '__main__':
    main()
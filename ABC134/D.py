def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))

    for i in range(N//2, 0, -1):
        sum_m = sum([A[i*j] for j in range(2, N//i+1)])
        if A[i] == 0:
            if sum_m % 2 == 1:
                A[i] = 1
        else:
            if sum_m % 2 == 1:
                A[i] = 0

    sum_b = sum(A)
    print(sum_b)
    if sum_b:
        ans = [str(i) for i, v in enumerate(A) if v == 1]
        print('\n'.join(ans))


if __name__ == "__main__":
    main()
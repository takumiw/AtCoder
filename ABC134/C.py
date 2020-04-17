def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    A_asc = sorted(A)
    m1 = A_asc[-1]
    m2 = A_asc[-2]

    if m1 == m2:
        print('\n'.join([str(m1) for _ in range(N)]))
    else:
        for a in A:
            if a != m1:
                print(m1)
            else:
                print(m2)


if __name__ == "__main__":
    main()

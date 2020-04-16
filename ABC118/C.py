def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) > 1:
        m = min(A)
        A = [a % m for a in A if a % m != 0]
        A.append((m))

    print(m)


if __name__ == "__main__":
    main()
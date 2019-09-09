def main():
    N = int(input())
    H = list(map(int, input().split()))
    M = 0
    count = 0
    s = H.pop(0)
    for h in H:
        if s >= h:
            count += 1
        else:
            M = max(M, count)
            count = 0
        s = h
    print(max(M, count))

if __name__ == "__main__":
    main()